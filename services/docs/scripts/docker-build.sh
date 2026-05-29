# Run from services/docs

# Build image
podman build -t localhost:5000/docs-service:latest .

# Test image locally
podman run -p 5000:5000 docs-service

# Push to local registry (if using local registry)
#docker push localhost:5000/docs-service:latest

# Apply to k3s
#kubectl apply -f k8s-manifest.yaml