from fmcapi import *
from re import search
from argparse import ArgumentParser

def get_args():
    '''
    Get args from CLI.
    '''
    parser = ArgumentParser(description='Get arguments for rmv_objects script.')
    parser.add_argument('server', type=str, help='IP or DNS of the FMC Server')
    parser.add_argument('username', type=str, help='Username for FMC.')
    parser.add_argument('password', type=str, help='Password for FMC.')
    parser.add_argument('object_type', type=str, help='Object type to remove. protocolport, ipnetwork, networkgroup are supported today.')
    parser.add_argument('regex', type=str, help='The regular expression to match objects to remove. Use double quotes around the pattern.')

    args = parser.parse_args()
    return args


def del_obj(obj1, result, regex):

    print('Let\'s delete some stuff! -->')

    del_count = 0

    for k in result['items']:
        
        if search(regex, k['name']):
            print("Deleting {}".format(k['name']))
            try:
                obj1.delete(id=k['id'])
                del_count = del_count + 1
            except TypeError:
                print("We can't delete objects that are in use.")
    
    if del_count:
        return del_count


def main():

    args = get_args()
    fmc_server = args.server
    username = args.username
    password = args.password
    object_type = args.object_type
    regex = args.regex

    object_type.lower()
    
    implemented_objects = ('protocolport', 'ipnetwork', 'networkgroup', 'iphost')

    if object_type in implemented_objects:

        with FMC(host=fmc_server, username=username, password=password, autodeploy=False) as fmc1:

            if object_type == 'protocolport':
                obj1 = ProtocolPort(fmc=fmc1)
                result = obj1.get()
                del_count = del_obj(obj1, result, regex)

            elif object_type == 'ipnetwork':
                obj1 = IPNetwork(fmc=fmc1)
                result = obj1.get()
                del_count = del_obj(obj1, result, regex)

            elif object_type == 'networkgroup':
                obj1 = NetworkGroup(fmc=fmc1)
                result = obj1.get()
                del_count = del_obj(obj1, result, regex)

            elif object_type == 'iphost':
                obj1 = IPHost(fmc=fmc1)
                result = obj1.get()
                del_count = del_obj(obj1, result, regex)

            print("Deleted {} {} object(s).".format(del_count, object_type))

    else:
        print('Not an implemented object type.')


if __name__ == '__main__':
    main()
