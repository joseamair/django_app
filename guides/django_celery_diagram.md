# How Django App and Celery works
How a Django + Celery dockerized should work

```mermaid
flowchart LR
    subgraph Message Provider
    Django["Django App"]
    end

    subgraph Message Broker
    Redis["Redis Broker"]
    end

    subgraph Celery Broker
    Celery["Celery Worker"]
    end

    subgraph Result Backend
    DB["Database"]
    end

    Django["Django App"]-->Redis["Redis Broker"]-->Celery["Celery Worker"]-->DB["Database"]
```

## Message Provider / Task Producer
Identify the task that needs to be send and run by the Celery server. Triggered by user actions, form submissions, or others actions.



