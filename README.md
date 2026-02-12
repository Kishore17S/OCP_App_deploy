# Simple Voting App for OpenShift

A lightweight, modern voting application built with Flask and designed for deployment on OpenShift Container Platform.

## 📊 What It Does

Users can vote between **Python** 🐍 and **JavaScript** ⚡. The app displays real-time voting percentages and updates automatically every 2 seconds.

## ✨ Features

- ✅ Simple one-page voting interface
- ✅ Real-time results with auto-refresh
- ✅ Responsive design with modern UI
- ✅ OpenShift-ready with health checks
- ✅ Runs as non-root user (secure)
- ✅ TLS/HTTPS enabled via OpenShift routes
- ✅ Resource limits configured
- ✅ Production-ready with Gunicorn

## 🏗️ Project Structure

```
.
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile             # Container build configuration
├── .dockerignore          # Files to exclude from Docker build
├── .gitignore             # Files to exclude from Git
├── README.md              # This file
├── templates/
│   └── index.html         # Main HTML page
├── static/
│   ├── style.css          # Stylesheets
│   └── script.js          # JavaScript for voting logic
└── openshift/
    ├── deployment.yaml    # Kubernetes deployment configuration
    ├── service.yaml       # Service definition (internal networking)
    └── route.yaml         # Route configuration (external access)
```

## 🚀 Deploying to OpenShift

### Prerequisites

- Access to an OpenShift cluster
- `oc` CLI tool installed ([Installation Guide](https://docs.openshift.com/container-platform/latest/cli_reference/openshift_cli/getting-started-cli.html))
- Git repository with this code

### Quick Deploy (Recommended)

This method lets OpenShift build the container image automatically from your GitHub repository:

```bash
# 1. Login to your OpenShift cluster
oc login https://your-openshift-cluster-url

# 2. Create a new project
oc new-project voting-app

# 3. Deploy from GitHub repository (replace with your repo URL)
oc new-app https://github.com/YOUR_USERNAME/voting-app.git \
  --name=voting-app \
  --strategy=docker

# 4. Expose the service to create an external route
oc expose svc/voting-app

# 5. Get your application URL
oc get route voting-app
```

You'll see output like:
```
NAME         HOST/PORT                                    PATH   SERVICES     PORT   TERMINATION
voting-app   voting-app-voting-app.apps.cluster.com             voting-app   8080   edge
```

Visit the URL to see your app! 🎉

### Alternative: Deploy with Custom Route

If you want a custom hostname or TLS configuration:

```bash
# Deploy the app
oc new-app https://github.com/YOUR_USERNAME/voting-app.git \
  --name=voting-app \
  --strategy=docker

# Apply custom route configuration
oc apply -f openshift/route.yaml

# Get the route
oc get route voting-app
```

### Using Pre-built YAML Manifests

If you prefer to use the YAML files directly:

```bash
# 1. Build the image first
oc new-build --binary --name=voting-app --strategy=docker
oc start-build voting-app --from-dir=. --follow

# 2. Apply all manifests
oc apply -f openshift/
```

**Note:** You'll need to update `deployment.yaml` line 19 to use the correct image reference.

## 💻 Local Development

### Run Locally with Python

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Visit http://localhost:8080
```

### Run Locally with Docker

```bash
# Build the image
docker build -t voting-app:latest .

# Run the container
docker run -p 8080:8080 voting-app:latest

# Visit http://localhost:8080
```

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main voting page |
| `/api/vote` | POST | Submit a vote (JSON: `{"choice": "python"}`) |
| `/api/results` | GET | Get current voting results |
| `/api/health` | GET | Health check endpoint |

## 🔧 Configuration

### Environment Variables

- `PORT` - Application port (default: 8080)
- `ENVIRONMENT` - Environment name (default: production)

### Resource Limits

Default resource configuration (defined in `deployment.yaml`):

- **Memory**: 128Mi (request) / 256Mi (limit)
- **CPU**: 100m (request) / 500m (limit)

Adjust these based on your needs by editing `openshift/deployment.yaml`.

## 📈 Scaling

### Manual Scaling

Scale to multiple replicas:

```bash
oc scale deployment/voting-app --replicas=3
```

### Auto-scaling

Enable horizontal pod autoscaling:

```bash
oc autoscale deployment/voting-app \
  --min=2 \
  --max=10 \
  --cpu-percent=80
```

⚠️ **Note:** This app uses in-memory storage for votes. If you scale to multiple replicas, each pod will have its own vote count. For production use with multiple replicas, implement Redis or a database backend.

## 🔒 Security Features

- ✅ Runs as non-root user (UID 1001)
- ✅ Security context with `allowPrivilegeEscalation: false`
- ✅ Dropped Linux capabilities
- ✅ TLS termination at route level
- ✅ Read-only root filesystem compatible

## 🐛 Troubleshooting

### Check Pod Status
```bash
oc get pods
```

### View Application Logs
```bash
oc logs -f deployment/voting-app
```

### Get Deployment Details
```bash
oc describe deployment voting-app
```

### Access Pod Shell
```bash
oc rsh deployment/voting-app
```

### Test Health Endpoint
```bash
# Get the route URL first
ROUTE_URL=$(oc get route voting-app -o jsonpath='{.spec.host}')

# Test health endpoint
curl https://$ROUTE_URL/api/health
```

### Common Issues

**Problem:** "Image pull failed"
- **Solution:** Check that the build completed successfully with `oc get builds`

**Problem:** "Pod keeps restarting"
- **Solution:** Check logs with `oc logs deployment/voting-app` and verify health endpoint returns 200

**Problem:** "Route not accessible"
- **Solution:** Verify route exists with `oc get route` and check firewall/DNS settings

## 🔄 Updating the Application

After making code changes:

```bash
# Trigger a new build from Git
oc start-build voting-app

# Watch the build progress
oc logs -f bc/voting-app

# New pods will automatically deploy when build completes
```

## 🗑️ Cleanup

Delete all resources:

```bash
oc delete all -l app=voting-app
```

Or delete the entire project:

```bash
oc delete project voting-app
```

## 📚 Learn More

- [OpenShift Documentation](https://docs.openshift.com/)
- [Kubernetes Concepts](https://kubernetes.io/docs/concepts/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

## 📄 License

MIT License - feel free to use this for learning and demos!

## 🤝 Contributing

This is a simple demo app, but feel free to fork and enhance it!

Ideas for improvements:
- Add database backend (PostgreSQL, MongoDB)
- Implement Redis for distributed voting
- Add user authentication
- Create admin dashboard
- Add more voting options
- Implement voting time limits

## 💡 About

Created as a simple, practical example for learning OpenShift deployment concepts. Perfect for workshops, demos, and getting started with containerized applications on OpenShift.
