# Lab: Deploy Flask Backend with Python Load Balancer on Kubernetes with AB Testing

In this lab, you'll deploy multiple instances of a Flask backend on Kubernetes, set up a Python-based load balancer, and perform load testing using Apache Benchmark (AB). By the end of the lab, you'll have a Kubernetes setup that distributes traffic to multiple backend instances, allowing you to test the load balancer's performance.

## Deliverables

- [ ] Show the TA the logs of one backend Pod in the MiniKube dashboard.
- [ ] Explain to the TA how the load balancer distributes requests to the backend instances.
- [ ] Show a screenshot of Apache Benchmark (AB) test output with performance metrics.
- [ ] Demonstrate using `minikube service` to access the load balancer if NodePort does not work.

---

## Lab Instructions

### Part 1: Set Up the Flask Backend Application

1. **Create the Flask Backend Application**:
   - Write a simple Flask application (`backend.py`) that responds with a personalized message based on a user ID.
   - **TODO**: Customize the response message and include a unique identifier for each backend instance.

2. **Containerize the Backend**:
   - Write a Dockerfile for the backend application.
   - **TODO**: Replace placeholder Docker Hub username with your own Docker Hub repository details.

3. **Build and Push Docker Image**:
   - Build and push the Docker image for the backend to your Docker Hub repository.
   - **TODO**: Use your Docker Hub username to create the image tag.

---

### Part 2: Deploy the Backend on Kubernetes

1. **Create Backend Deployment and Service Files**:
   - Define a deployment YAML file for the backend with multiple replicas.
   - Define a service YAML file to expose the backend internally within the Kubernetes cluster.
   - **TODO**: Replace placeholders in the YAML files with your Docker Hub image name and specify unique identifiers as needed.

2. **Apply the Backend Configuration**:
   - Deploy the backend application and service on Kubernetes by applying the YAML files.

---

### Part 3: Set Up the Python Load Balancer

1. **Create the Load Balancer Application**:
   - Write a Python load balancer (`load_balancer.py`) using Flask that distributes requests to backend instances in a round-robin fashion.
   - **TODO**: Add multiple backend URLs if desired, and customize the load balancer response to indicate which backend instance is handling each request.

2. **Containerize the Load Balancer**:
   - Write a Dockerfile for the load balancer application.
   - **TODO**: Replace Docker Hub username with your own repository details.

3. **Build and Push Load Balancer Docker Image**:
   - Build and push the load balancer Docker image to your Docker Hub repository.

---

### Part 4: Deploy the Load Balancer on Kubernetes

1. **Create Load Balancer Deployment and Service Files**:
   - Define a deployment YAML file for the load balancer with one replica.
   - Define a NodePort service YAML file to expose the load balancer on an accessible port.
   - **TODO**: Replace placeholders in the YAML files with your Docker Hub image name and specify unique service names as needed.

2. **Apply the Load Balancer Configuration**:
   - Deploy the load balancer service on Kubernetes by applying the YAML files.

---

### Part 5: Access and Test the Load Balancer

1. **Access via NodePort**:
   - Use `minikube ip` to get the MiniKube IP and access the load balancer using NodePort.
   - **TODO**: Test the setup with a `curl` command to ensure the load balancer is reachable and distributing requests correctly.

2. **Use `minikube service` (If NodePort Does Not Work)**:
   - If NodePort access isn’t working, use `minikube service` to create a tunnel to the load balancer.
   - **TODO**: Use the URL provided by `minikube service` to access the load balancer and verify round-robin request distribution.

3. **Launch MiniKube Dashboard**:
   - Run `minikube dashboard` in a separate terminal to open the MiniKube dashboard for monitoring the status of the Pods and services.

---

### Part 6: AB Testing with Apache Benchmark

1. **Run Basic AB Test**:
   - Use Apache Benchmark to send a series of requests to the load balancer.
   - **TODO**: Run a basic AB test with 100 requests and 10 concurrent connections.

2. **Perform High-Load AB Test (Optional)**:
   - Increase the request count and concurrency level to simulate high traffic.
   - **TODO**: Observe load balancer performance under high load and check backend Pod distribution.

3. **Observe Load Balancer Logs (Optional)**:
   - Monitor the backend logs in real-time to verify that the load balancer distributes requests evenly across backend instances.

---

## Testing the Load Balancer

### Calling the Load Balancer with `curl`

Use the following `curl` command to test your load balancer setup, replacing `<minikube-ip>` and `<some-port>` with the appropriate IP and port:

```bash
curl "http://<minikube-ip>:30080/?user_id=Alice"
