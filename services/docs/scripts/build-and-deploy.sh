# Run from services/docs

# Build image
podman build -t localhost:5000/docs-service:latest .

# Test image locally
podman run -p 5000:5000 docs-service

# Push to local registry (if using local registry)
docker push localhost:5000/docs-service:latest

# Load the image into k3s's containerd.
docker save localhost:5000/docs-service:latest | k3s ctr images import -
k3s ctr images ls | grep docs-service

# Apply to k3s
kubectl apply -f k8s-manifest.yaml

# Port-forward the service to access it at http://localhost:5000
kubectl -n archive port-forward svc/docs-service 5000:80
