# Lab 9: Kubernetes
...

To receive credit for this lab, show your work to the TA during recitation.

## Deliverables
- [ ] ...
- [ ] ...
- [ ] ...

## Getting started


- Install MiniKube https://minikube.sigs.k8s.io/docs/start/ (i.e. `brew install minikube` for MacOS)
- `minikube start`
- `kubectl get po -A` to show stats
- `kubectl apply -f deployment.yml`
- `kubectl expose deployment nginx-deployment --type=NodePort --port=80`

