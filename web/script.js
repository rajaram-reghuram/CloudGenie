async function generateCommand() {
    const commandType = document.getElementById('commandType').value;
    const userInput = document.getElementById('userInput').value;

    const endpointMap = {
        terraform: '/generate-terraform',
        cloudformation: '/generate-cloudformation',
        k8s_yaml: '/generate-k8s-yaml',
        dockerfile: '/generate-dockerfile',
        aws_cli: '/generate-aws-cli',
        azure_cli: '/generate-azure-cli',
        kubectl: '/generate-kubectl'
    };

    const endpoint = endpointMap[commandType];

    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ config: userInput })
        });

        const result = await response.json();
        document.getElementById('output').innerText = result;
    } catch (error) {
        document.getElementById('output').innerText = '❌ Error generating command. Please try again.';
    }
}
