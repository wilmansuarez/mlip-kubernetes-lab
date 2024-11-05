# Lab 9: Advanced Kubernetes Deployment with Multiple Services and Load Balancing

In this lab, you will go beyond deploying a single service. You'll set up multiple instances of an application with different services, simulate load balancing, and observe how Kubernetes distributes traffic. You will also experience Kubernetes' self-healing, autoscaling, and traffic management capabilities.

## Objectives
- Deploy multiple services in Kubernetes
- Set up a load balancer to distribute traffic across services
- Observe how Kubernetes handles updates, self-healing, and autoscaling

## Deliverables
- [ ] Show the TA the logs of one Pod in the MiniKube dashboard
- [ ] Explain to the TA how Kubernetes deploys updates and manages multiple services
- [ ] Show a screenshot of the crashed Pod(s)
- [ ] Take a screenshot of the load balancer distributing traffic across multiple services

---

## Getting Started
1. **Start Docker**
2. **Install MiniKube**: Follow instructions [here](https://minikube.sigs.k8s.io/docs/start/).
3. **Start MiniKube**: Run `minikube start`
4. Verify MiniKube: Run `kubectl get po -A` to ensure it's running.

---

### Step 1: Apply the Deployment and Multiple Service Configurations
You will configure multiple instances of a service and a load balancer.

1. **Download the YAML files**:
   - `deployment.yaml`: Manages the desired state of your app, including replica counts and update strategy.
   - `service1.yaml` and `service2.yaml`: Create two separate services with different configurations or ports.
   - `loadbalancer-service.yaml`: Sets up a LoadBalancer service to route traffic between services.

2. **Apply Configurations**:
   - Deploy the services and load balancer:
     ```bash
     kubectl apply -f deployment.yaml
     kubectl apply -f service1.yaml
     kubectl apply -f service2.yaml
     kubectl apply -f loadbalancer-service.yaml
     ```
   - Verify services with `kubectl get services`. You should see both services and the load balancer listed.

---

### Step 2: Set Up a Load Balancer
1. **Test the Load Balancer**:
   - Access the load balancer URL. Refresh the page multiple times to observe which pod or service instance responds to each request.
   - **Deliverable**: Take a screenshot showing the distributed traffic in the dashboard.

---

### Step 3: Start the Service and Observe
1. **Launch MiniKube Dashboard**: Run `minikube dashboard`.
2. **Verify Service Logs**:
   - In the MiniKube dashboard, find one of the pods for `flask-app`.
   - View and show the logs to the TA.
   - **Deliverable**: Take a screenshot of the logs.

---

### Step 4: Deploy an Update and Observe Traffic Distribution
1. **Update the `deployment.yaml`**:
   - Change the Docker image version from `1.0.0` to `1.0.1`.
   - Apply the update:
     ```bash
     kubectl apply -f deployment.yaml
     ```
2. **Observe the Update**: Switch to the dashboard to observe how Kubernetes manages traffic and deploys updates.
   - **Deliverable**: Explain to the TA how traffic is balanced across updated services and how Kubernetes handles updates.

---

### Step 5: Test Auto-Restarts and Self-Healing
1. **Simulate a Crash**: Access the `<endpoint>/crash` URL to crash a service.
2. **Observe Self-Healing**: Quickly return to the dashboard and watch the Pods restart automatically.
   - **Deliverable**: Capture a screenshot of the crashed and restarted Pods.

---

### Step 6: Enable Autoscaling (Optional)
1. **Set up Autoscaling**:
   - Install the metrics-server addon:
     ```bash
     kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
     minikube addons enable metrics-server
     ```
   - Confirm it's running with:
     ```bash
     kubectl get deployment metrics-server -n kube-system
     ```
2. **Configure Autoscaling**:
   - Set up autoscaling for your deployment:
     ```bash
     kubectl autoscale deployment flask-app --min=2 --max=5 --cpu-percent=70
     ```
   - Verify autoscaling with `kubectl get hpa`.

3. **Stress Test**:
   - Use `ab -n 1000 -c 10 <load-balancer-endpoint>` to simulate heavy traffic.
   - Observe in the dashboard how autoscaling adds more pods.
   - **Deliverable**: Take a screenshot of the auto-scaled Pods list.

---

### Troubleshooting
- `kubectl get pods` to view running Pods
- `kubectl logs <pod-name>` to see Pod logs
- `kubectl delete pods -l app=flask-app` to manually delete and restart Pods
