## Containerized solutions

### General information

_Image_:

A package of an application and its dependencies:

- Lightweight.
- Portable.

**Azure Container Registry** (ACR) is a managed registry service based on the open-source Docker Registry 2.0. Create and maintain Azure container registries to store and manage your container images and related artifacts. (There are other solutions like Docker Hub).

---

### Service tiers

![az-containerized-solutions-1](../azure_containerized_solutions/images/az-containerized-solutions-1.png)

---

### Storage capabilities

All Azure Container Registry tiers benefit from advanced Azure storage features like encryption-at-rest for image data security and geo-redundancy for image data protection:

- Encryption-at-rest.
- Regional storage.
- Geo-replication (Only for the Premium tier).
- Zone redundancy.
- Scalable storage.

---

### Build and manage containers with tasks

ACR Tasks supports several scenarios to build and maintain container images and other artifacts:

- _Quick task_ - Build and push a single container image to a container registry on-demand, in Azure, without needing a local Docker Engine installation. Think `docker build`, `docker push` in the cloud.
- _Automatically triggered tasks_ - Enable one or more _triggers_ to build an image:
  - Trigger on source code update.
  - Trigger on base image update.
  - Trigger on a schedule.
- _Multi-step task_ - Extend the single image build-and-push capability of ACR Tasks with multi-step, multi-container-based workflows.

---

### Elements of a Dockerfile

```Dockerfile
# Use the .NET 6 runtime as a base image
FROM mcr.microsoft.com/dotnet/runtime:6.0

# Set the working directory to /app
WORKDIR /app

# Copy the contents of the published app to the container's /app directory
COPY bin/Release/net6.0/publish/ .

# Document that the application listens on port 80 (does not publish it)
EXPOSE 80

# Set the command to run when the container starts
CMD ["dotnet", "MyApp.dll"]
```

---

### Execution example

Creation of ACR:

![az-containerized-solutions-2](../azure_containerized_solutions/images/az-containerized-solutions-2.png)

The process of bulding and pushing an image:

![az-containerized-solutions-3](../azure_containerized_solutions/images/az-containerized-solutions-3.png)

Execution:

![az-containerized-solutions-4](../azure_containerized_solutions/images/az-containerized-solutions-4.png)

---

## Run container images in Azure Container Instances

### General information

Azure Container Instances (ACI) is a great solution for any scenario that can operate in isolated containers, including simple applications, task automation, and build jobs. Here are some of the benefits:

- Fast startup.
- Container access.
- Hypervisor-level security.
- Customer data.
- Custom sizes.
- Persistent storage.
- Linux and Windows.

The following diagram shows an example of a container group that includes multiple containers:

![az-containerized-solutions-5](../azure_containerized_solutions/images/az-containerized-solutions-5.png)

---

### Restart policy

![az-containerized-solutions-6](../azure_containerized_solutions/images/az-containerized-solutions-6.png)

---

### Mount an Azure file share in ACI

By default, Azure Container Instances are stateless. If the container crashes or stops, all of its state is lost. To persist state beyond the lifetime of the container, you must mount a volume from an external store.

To mount multiple volumes in a container instance, you must deploy using an _Azure Resource Manager template_ or a _YAML file_.

---

## Implement containerized solutions

TODO

---
