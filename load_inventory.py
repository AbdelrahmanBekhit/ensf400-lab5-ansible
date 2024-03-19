from ansible_runner import Runner

# Define inventory content
inventory_content = '''
[app_group]
managedhost-app-1 ansible_host=your_host_ip_1
managedhost-app-2 ansible_host=your_host_ip_2
managedhost-app-3 ansible_host=your_host_ip_3
'''

# Save inventory to a file
with open('inventory.yml', 'w') as inventory_file:
    inventory_file.write(inventory_content)

# Run ping command using ansible-runner
runner = Runner(inventory='inventory.yml', playbook='ping.yml')
results = runner.run()

# Print the names, IP addresses, group names, and ping results
for host in results['contacted'].keys():
    print(f"Name: {host}")
    print(f"IP Address: {results['contacted'][host]['ansible_host']}")
    for group in results['contacted'][host]['group_names']:
        print(f"Group: {group}")
    print(f"Ping Result: {results['contacted'][host]['ping']}")
    print()
