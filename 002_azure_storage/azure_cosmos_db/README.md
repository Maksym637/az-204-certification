## Azure Cosmos DB

### General information

Azure Cosmos DB is a fully managed NoSQL database designed to provide low latency, elastic scalability of throughput, well-defined semantics for data consistency, and high availability.

You can configure your databases to be globally distributed and available in any of the Azure regions.

---

### The resource hierarchy

**!** Currently, you can create a maximum of 50 Azure Cosmos DB accounts under an Azure subscription.

**Key Terms**:

| Term                  | Meaning                                                       |
| --------------------- | ------------------------------------------------------------- |
| **Database**          | Logical grouping of containers                                |
| **Container**         | Stores JSON items; horizontally scalable                      |
| **Item**              | A JSON document                                               |
| **Partition Key**     | Determines how data is distributed across physical partitions |
| **Throughput (RU/s)** | Cost measure for operations                                   |

**!Important:** Choosing a good **partition key** (high cardinality, even distribution) is critical for performance and cost.

Example:

Suppose you store order documents:

```json
{
  "orderId": "123",
  "userId": "u321",
  "amount": 99.5
}
```

If your _partition key_ = `"userId"`
Then:

- All orders from `"u321"` go to the same logical partition
- Each user gets their own partition
- High cardinality (thousands of users)
- Even load (users order at similar rates)

So, this is a _good_ partition key

The following image shows the hierarchy of different entities in an Azure Cosmos DB account:

![az-cosmos-db-1](../azure_cosmos_db/images/az-cosmos-db-1.png)

---

### Consistency levels

| Consistency Level     | Guarantee                                  |
| --------------------- | ------------------------------------------ |
| **Strong**            | Reads always return latest committed write |
| **Bounded Staleness** | Reads lag behind by a time window          |
| **Session** (Default) | Read your own writes                       |
| **Consistent Prefix** | Guaranteed ordered writes (1, 2, 3, 4, 5)  |
| **Eventual**          | No ordering guarantee (5, 2, 3, 1, 4)      |

![az-cosmos-db-2](../azure_cosmos_db/images/az-cosmos-db-2.png)

---

### Supported APIs

- API for NoSQL.
- API for MongoDB.
- API for PostgreSQL.
- API for Apache Cassandra.
- API for Apache Gremlin.
- API for Table.

---

### Request units (RU)

Request unites (RUs) - a unit of measurement used to express the cost of all database operations in Azure Cosmos DB.

![az-cosmos-db-3](../azure_cosmos_db/images/az-cosmos-db-3.png)

---
