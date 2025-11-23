## Azure Functions

### General information

Azure Functions is a serverless solution that allows you to write less code, maintain less infrastructure, and save on costs. Instead of worrying about deploying and maintaining servers, the cloud infrastructure provides all the up-to-date resources needed to keep your applications running.

Azure Functions supports _triggers_, which are ways to start execution of your code, and bindings, which are ways to simplify coding for input and output data.

---

### Azure Functions vs. Azure Logic Apps

Both Functions and Logic Apps are Azure Services that enable serverless workloads. Azure Functions is a serverless compute service, whereas Azure Logic Apps is a serverless workflow integration platform. Both can create complex orchestrations. An orchestration is a collection of functions or steps, called actions in Logic Apps, that are executed to accomplish a complex task.

Durable functions information -> https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview?tabs=in-process%2Cnodejs-v3%2Cv1-model&pivots=python

![az-functions-1](../azure_functions/images/az-functions-1.png)

---

### Azure Functions vs. Azure WebJobs

Like Azure Functions, Azure App Service WebJobs with the WebJobs SDK is a code-first integration service that is designed for developers. Both are built on Azure App Service and support features such as source control integration, authentication, and monitoring with Application Insights integration.

![az-functions-2](../azure_functions/images/az-functions-2.png)

---

### Hosting options

Following is a summary of the benefits of the various hosting options:

1. _Consumption plan:_ The Consumption plan is the default hosting plan. Pay for compute resources only when your functions are running (pay-as-you-go) with automatic scale. On the Consumption plan, instances of the Functions host are dynamically added and removed based on the number of incoming events.
2. _Flex Consumption plan:_ Get high scalability with compute choices, virtual networking, and pay-as-you-go billing. On the Flex Consumption plan, instances of the Functions host are dynamically added and removed based on the configured per instance concurrency and the number of incoming events. You can reduce cold starts by specifying the number of pre-provisioned (always ready) instances. Scales automatically based on demand.
3. _Premium plan:_ Automatically scales based on demand using prewarmed workers, which run applications with no delay after being idle, runs on more powerful instances, and connects to virtual networks.
4. _Dedicated plan:_ Run your functions within an App Service plan at regular App Service plan rates. Best for long-running scenarios where Durable Functions can't be used.
5. _Container Apps:_ Create and deploy containerized function apps in a fully managed environment hosted by Azure Container Apps.

---

### Scale Azure Functions

![az-functions-3](../azure_functions/images/az-functions-3.png)

---

## Develop Azure Functions

### General information

**!** All of the functions in a function app share the same pricing plan, deployment method, and runtime version.

---

### Local project files

A Functions project directory contains the following files in the project root folder, regardless of language:

- `host.json`.
- `local.settings.json`.
- Other files in the project depend on your language and specific functions.

---

### Triggers and Bindings

A trigger defines how a function is invoked and a function must have exactly one trigger. Triggers have associated data, which is often provided as the payload of the function.

...

Binding to a function is a way of declaratively connecting another resource to the function; bindings might be connected as input bindings, output bindings, or both. Data from bindings is provided to the function as parameters.

...

All triggers and bindings have a direction property in the _function.json_ file:

- `in` -> for triggers.
- `in` and `out` -> for bindings.
- `inout` -> for bindings.

---

### Example execution

...

---
