\# Azure Cloud Monitoring API



A Python Flask-based cloud monitoring API deployed on \*\*Microsoft Azure App Service\*\*.



The application collects real-time CPU, memory, and uptime information and evaluates resource usage against configurable warning and critical thresholds.



!\[Azure Cloud Monitoring API Architecture](architecture.png)



\## 🚀 Live Application



\*\*Azure App Service\*\*



`https://harsh-cloud-monitoring-api-fra7h2gjfybyf0ab.centralindia-01.azurewebsites.net`



\## 🛠️ Technologies Used



\* Python 3.12

\* Flask 3.1.3

\* Gunicorn

\* psutil

\* Microsoft Azure App Service

\* Azure Application Insights

\* Azure CLI



\## 📡 API Endpoints



\### Health Check



\*\*GET `/health`\*\*



Used to verify that the API is healthy.



Example response:



```json

{

&#x20; "service": "azure-cloud-monitoring-api",

&#x20; "status": "healthy"

}

```



\### Service Status



\*\*GET `/status`\*\*



Returns the current application status and hosting environment.



Example response:



```json

{

&#x20; "environment": "Azure App Service",

&#x20; "service": "azure-cloud-monitoring-api",

&#x20; "status": "running"

}

```



\### System Metrics



\*\*GET `/metrics`\*\*



Returns real-time CPU, memory, uptime, threshold information, and the overall service status.



Example response:



```json

{

&#x20; "cpu": {

&#x20;   "critical\_threshold": 90,

&#x20;   "status": "healthy",

&#x20;   "usage\_percent": 14.1,

&#x20;   "warning\_threshold": 70

&#x20; },

&#x20; "memory": {

&#x20;   "critical\_threshold": 90,

&#x20;   "status": "warning",

&#x20;   "usage\_percent": 72.6,

&#x20;   "warning\_threshold": 70

&#x20; },

&#x20; "memory\_available\_mb": 523.78,

&#x20; "memory\_used\_mb": 1070.69,

&#x20; "service": "azure-cloud-monitoring-api",

&#x20; "status": "warning",

&#x20; "uptime\_seconds": 2212

}

```



> The CPU, memory, and uptime values change dynamically based on the running application.



\## ⚙️ Monitoring Logic



The API evaluates CPU and memory usage using three states:



| Resource Usage | Status   |

| -------------- | -------- |

| Below 70%      | Healthy  |

| 70%–89%        | Warning  |

| 90% or higher  | Critical |



The overall service status is determined by the most severe resource status.



For example:



\* CPU healthy + memory healthy → \*\*Healthy\*\*

\* CPU healthy + memory warning → \*\*Warning\*\*

\* CPU warning + memory healthy → \*\*Warning\*\*

\* CPU critical + memory healthy → \*\*Critical\*\*



\## ☁️ Azure Architecture



The application is hosted on \*\*Azure App Service\*\* using Python, Flask, and Gunicorn.



```text

&#x20;                        Internet

&#x20;                           |

&#x20;                           v

&#x20;                 +-------------------+

&#x20;                 |   Azure App       |

&#x20;                 |     Service       |

&#x20;                 |                   |

&#x20;                 | Python + Flask    |

&#x20;                 |    + Gunicorn     |

&#x20;                 +---------+---------+

&#x20;                           |

&#x20;                           v

&#x20;                  +----------------+

&#x20;                  |    REST API     |

&#x20;                  +--------+--------+

&#x20;                           |

&#x20;            +--------------+--------------+

&#x20;            |              |              |

&#x20;            v              v              v

&#x20;         /health        /status       /metrics

&#x20;                                          |

&#x20;                                 +--------+--------+

&#x20;                                 |                 |

&#x20;                                 v                 v

&#x20;                           CPU Monitoring    Memory Monitoring

&#x20;                                 |                 |

&#x20;                                 +--------+--------+

&#x20;                                          |

&#x20;                                          v

&#x20;                                  Threshold Engine

&#x20;                                          |

&#x20;                             +------------+------------+

&#x20;                             |            |            |

&#x20;                             v            v            v

&#x20;                          Healthy      Warning      Critical



&#x20;                           Azure Application Insights

&#x20;                                     |

&#x20;                                     v

&#x20;                              Application Monitoring

```



Azure Application Insights is connected to the App Service for application monitoring and observability.



\## 📦 Project Structure



```text

azure-cloud-monitoring-api/

│

├── app.py

├── requirements.txt

├── README.md

└── architecture.png

```



> `deploy.zip` is used locally for Azure deployment and should not be committed to the GitHub repository.



\## 💻 Run Locally



Clone the repository and enter the project directory:



```bash

cd azure-cloud-monitoring-api

```



Install the dependencies:



```bash

pip install -r requirements.txt

```



Run the application:



```bash

python app.py

```



The API will run locally on:



```text

http://127.0.0.1:5000

```



\### Test the Health Endpoint



```bash

curl http://127.0.0.1:5000/health

```



\### Test the Status Endpoint



```bash

curl http://127.0.0.1:5000/status

```



\### Test the Metrics Endpoint



```bash

curl http://127.0.0.1:5000/metrics

```



\## 🚀 Production Server



The Azure App Service uses \*\*Gunicorn\*\* as the production WSGI server:



```text

gunicorn --bind=0.0.0.0:8000 app:app

```



\## ☁️ Azure Deployment



The application was deployed to Azure App Service using Azure CLI.



Example deployment command:



```powershell

az webapp deploy `

&#x20; --name harsh-cloud-monitoring-api `

&#x20; --resource-group rg-cloud-monitoring-dev `

&#x20; --src-path "C:\\cloud-monitoring-api\\deploy.zip" `

&#x20; --type zip

```



The application is deployed in the \*\*Central India\*\* Azure region.



\## 📊 Features



\* Real-time CPU monitoring

\* Real-time memory monitoring

\* Application uptime monitoring

\* CPU warning threshold

\* CPU critical threshold

\* Memory warning threshold

\* Memory critical threshold

\* Overall service status

\* REST API endpoints

\* Azure App Service deployment

\* Gunicorn production server

\* Azure Application Insights integration

\* Azure CLI deployment and management



\## 🎓 Skills Demonstrated



This project demonstrates practical experience with:



\* Python

\* Flask REST APIs

\* System monitoring with `psutil`

\* API health checks

\* Resource threshold evaluation

\* Microsoft Azure App Service

\* Azure CLI

\* Gunicorn

\* Python dependency management

\* Azure Application Insights

\* Cloud deployment troubleshooting

\* API testing with `curl`



\## 🔮 Future Improvements



Potential future improvements include:



\* Azure Monitor alerts

\* Email or Microsoft Teams notifications

\* Historical metrics storage

\* Monitoring dashboard

\* Azure Functions integration

\* Docker containerization

\* GitHub Actions CI/CD

\* Automated testing



\## 📌 Project Status



\*\*Version 1.0 — Completed\*\*



The monitoring API is deployed and running successfully on Microsoft Azure App Service.



