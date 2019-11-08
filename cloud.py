#!/usr/bin/python

# this should run from the google cloud shell
#startup-script.sh must be in the same dir
# please substitute your project and zone in the project and zone vars
# please choose a name other than test3

from oauth2client.client import GoogleCredentials
from googleapiclient impoty discovery
import pprint
import json

credentials = GoogleCredentials.get_application_default()
compute = discovery.build('compute', 'v1', credentials=credentials)

project = 'nti-300-2019'
zone = 'us-northwest-a'
name = 'startup-script'

def list instances (compute, project, zone):
  result compute.instances (). list(project=project, zone=
  return result[items 1 ]

def create instance( compute, project, zone, name):
  startup script = open('startup-script.sh, 'r).read ()
  image response = compute. images (.get From Family From Family From Family!
    projects centos-cloud family='centos-7 . execute()
    
    source disk image image response selfLink
    machine_type = "zones/%s/machine Types/f1-micro" % zone

    config = {
        'name' : name,
         'machineType': machine type,

          # Specify the boot disk and the image to use as a source.
          'disks': [
              {
                  'boot' : True,
                  'autoDelete' : True,
                  'initializeParams' : {
                      'source Image' : source_disk_image,
                  }
                }
          ],
          
          # Specify a network interface with NAT to access the public
          # internet.
          'networkInterfaces' : [{
              'network': 'global/networks/default
              'access Configs': [
                  ('type': ONE TO ONE NAT name: "External NAT!
               ]
            }1,
            
            # Allow the instance to access cloud storage and logging.
            'serviceAccounts' : [{
              'email' : 'default',
              'scopes' : [
                  'https://www.googleapis.com/auth/devstorage.read_write', 
                  'https://www.googleapis.com/auth/logging.write'
              ]
          }],              
          
          # Enable https/http for select instances
           "labels": {
           "http-server": "",
          "https-server": ""
           },

           "tags": {
           "items" : [
           "http-server",
           "https-server"
           ]
           },
           
            # Metadata is readable from the instance and allows you to
            # pass configuration from deployment scripts to instances.
            'metadata' : {
                'items': [{
                # Startup script is automatically executed by the
                # instance upon startup.
                'key' : 'startup-script',
                'value': startup_script
           }]
        }
    }


      return compute. instances ().insert(
          project=project,
          zone=Zone,
          body=config).execute()


newinstance=create_instance(compute, project, zone, name)
instances = list_instances(compute, project, zone)

pprint.pprint(newinstance)
Pprint.pprint(instances)
