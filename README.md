# Simple Voting App for OpenShift

A lightweight voting application built with Flask and designed for deployment on OpenShift Container Platform.

## � GitHub Commands

### First Time Push
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/yourrepo.git
git branch -M main
git push -u origin main
```

### Subsequent Pushes
```bash
git add .
git commit -m "Your commit message"
git push
```

### Push Specific File
```bash
git add openshift/deployment.yaml
git commit -m "Add OpenShift deployment YAML"
git push
```

---

## 🐳 Build Image in Docker Hub

### Prerequisites
- Login to Docker Hub website

### Build and Push Commands
```bash
# Build Docker image
docker build -t kishore17s/ocp-app-deploy:latest .

# Push to Docker Hub
docker push kishore17s/ocp-app-deploy:latest
```

---

## � Deploy in OpenShift

### Deployment Steps
```bash
# 1. Login to OpenShift
oc login <your-openshift-url>
oc project your-project-name

# 2. Build Docker image (with correct architecture)
docker build --platform linux/amd64 -t kishore17s/ocp-app-deploy:latest .

# 3. Push to Docker Hub
docker push kishore17s/ocp-app-deploy:latest

# 4. Apply Deployment
oc apply -f openshift/deployment.yaml

# 5. Apply Service
oc apply -f openshift/service.yaml

# 6. Apply Route
oc apply -f openshift/route.yaml

# 7. Check deployment status
oc get pods

# 8. Get route URL
oc get route voting-app

# 9. Check logs (if needed)
oc logs voting-app-xxxxx
```

---

## 📄 License

MIT License - feel free to use this for learning and demos!
