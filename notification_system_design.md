## Stage 1

## API 

## Get Notification

GET/notification/{studentID}

response:
{
    "notification":[
        {
            "id":1,
            "type":"some",
            "message":"eg",
            "isread":false
        }
    ]
}

## Mark as Read

POST /notification


{
    "studentID":111,
    "type":"eg",
    "message":"eg"
}

## Real time Notification

# I will use websockets for real time notification updates so users receive notification instantly without refresh

## Stage 2

## Database Choice

I will use Postgresql because notification data is structured data and postgress supports faster indexing and scaling efficiently

## Schema

CREATE TABLE notifications (
    id UUID PRIMARY KEY,
    studentId INT NOT NULL,
    type VARCHAR(255),
    message TEXT,
    isRead BOOLEAN DEFAULT FALSE,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



## Stage 3

The query is correct, but it becomes slow because the notifications table is very huge

sql

SELECT * FROM notifications
WHERE studentID = 1042 AND isRead = false
ORDER BY createdAt DESC;


I would add this index:

sql
CREATE INDEX idx_notifications
ON notifications(studentID, isRead, createdAt DESC);


Adding indexes to every column makes the query slower

## Placement Notifications Query

sql
SELECT DISTINCT studentID
FROM notifications
WHERE notificationType = 'Placement'
AND createdAt >= NOW() - INTERVAL '7 days';




## Stage 4

Fetching notifications on every page load increases Database so we can add redis or memcache,pagination or websockets too.



## Stage 5

The current approach is slow because notifications are sent one by one so we can use queues and worker services.

Flow:

HR Action → Queue → Workers → Email/App Notifications

