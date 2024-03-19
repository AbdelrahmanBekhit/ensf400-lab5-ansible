from ansible_runner import Runner

# Run the hello.yml playbook using ansible-runner
runner = Runner(inventory='inventory.yml', playbook='hello.yml')
results = runner.run()

# Print the results
print(results)
