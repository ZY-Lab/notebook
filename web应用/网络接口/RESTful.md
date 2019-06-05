##RESTful 

###一、介绍

REST，即Representational State Transfer的缩写。RESTful架构，是目前最流行的一种互联网软件架构。它结构清晰、符合标准、易于理解、扩展方便，基于这个风格设计的软件可以更简洁，更有层次，更易于实现缓存等机制，所以正得到越来越多网站的采用。如果一个架构符合REST原则，就称它为RESTful架构。

###二、RESTful API应遵循的原则  
###1、协议

API与用户的通信协议，总是使用HTTPs协议。

###2、域名

应该尽量将API部署在专用域名之下。

```
https://api.example.com
```
如果确定API很简单，不会有进一步扩展，可以考虑放在主域名下。
```
https://example.org/api/ 
```
###3、版本(Versioning)

应该将API的版本号放入URL。
```
https://api.example.com/v1/ 
```
另一种做法是，将版本号放在HTTP头信息中，但不如放入URL方便和直观。Github采用这种做法。  注：需要注意版本规划，以便以后API的升级和维护。使得API版本变得强制性，不要发布无版本的API，使用简单数字，避免小数点如2.5。

###4、路径(Endpoints) 

路径表示API的具体网址URL。在RESTful架构中，每个URL代表一种资源（resource），所以网址中不能有动词，只能有名词，而且所用的名词往往与代表的对象名称对应。一般来说，某一同种记录的”集合”（collection），所以API中的名词也应该使用复数。

####**具体细则：**

#####**1、使用名词而不是动词。**
举例来说，某个URL是/cards/show/1，其中show是动词，这个URL就设计错了，正确的写法应该是/cards/1，然后用GET方法表示show。如果某些动作是HTTP动词表示不了的，你就应该把动作做成一种资源。

比如网上汇款，**从账户1向账户2汇款500元**：

**错误**的URI是：
```
POST /accounts/1/transfer/500/to/2
```
**正确**的写法是把动词transfer改成名词transaction，资源不能是动词，但是可以是一种服务：
```
POST /transaction?from=1&to=2&amount=500.00
```

#####**2、使用复数名词。**

不要混淆名词单数和复数，为了保持简单，只对所有资源使用复数。  举例：

**/cars 而不是 /car
/users 而不是 /user
/products 而不是 /product
/settings 而不是 /setting**

#####**3、使用子资源表达关系。**

如果一个资源与另外一个资源有关系，使用子资源。  举例： 

**GET /cars/911/drivers/   返回 car 911的所有司机
GET /cars/911/drivers/8    返回 car 911的8号司机 **

#####**5、HTTP动词(HTTP Verbs)**

对于资源的具体操作类型，由HTTP动词表示。

**常用的HTTP动词有下面五个：**
- GET（SELECT）：从服务器取出资源（一项或多项）。
- POST（CREATE）：在服务器新建一个资源。
- PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。
- PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）。
- DELETE（DELETE）：从服务器删除资源。  

**还有两个不常用的HTTP动词。**
- HEAD：获取资源的元数据。
- OPTIONS：获取信息，关于资源的哪些属性是客户端可以改变的。

 **注**：Get方法和查询参数不应该涉及状态改变。使用PUT, POST 和DELETE方法而不是 GET 方法来改变状态。
 
 
#####**6、过滤信息（Filtering）**

 如果记录数量很多，服务器不可能都将它们返回给用户。API应该提供参数，过滤返回结果。为集合提供过滤、排序、选择和分页等功能。  
 
 下面是一些常见的参数。
- ?limit=10：指定返回记录的数量 • ?offset=10：指定返回记录的开始位置。
- ?pageNumber=2&perSize=100：指定第几页，以及每页的记录数。
- ?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。
- ?animal_type_id=1：指定筛选条件  

参数的设计允许存在冗余，即允许API路径和URL参数偶尔有重复。比如，GET /zoo/ID/animals 与 GET /animals?zoo_id=ID 的含义是相同的  

**注**：  ①移动端能够显示其中一些字段，它们其实不需要一个资源的所有字段，给API消费者一个选择字段的能力，这会降低网络流量，提高API可用性。  ②为了将总数发给客户端，使用订制的HTTP头： X-Total-Count.

#####**7、状态码（Status Codes）**

服务器向用户返回的状态码和提示信息，常见的有以下一些（方括号中是该状态码对应的HTTP动词）。
-  **200** OK - [GET]：服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）。 
-  **201** CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
-  **202** Accepted - [*]：表示一个请求已经进入后台排队（异步任务） 
-  **204** NO CONTENT - [DELETE]：用户删除数据成功。 
-  **400** INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。 
-  **401** Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
-  **403** Forbidden - [*]：表示用户得到授权（与401错误相对），但是访问是被禁止的。
-  **404** NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
-  **406** Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。 
-  **410** Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
-  **422** Unprocesable entity - [POST/PUT/PATCH]：当创建一个对象时，发生一个验证错误。
-  **500** INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。

#####**8、错误处理（Error handling）**
如果状态码是4xx，就应该向用户返回出错信息。尽量使用详细的错误包装信息：  

```json
{
    "errors":[
        {
            "userMessage":"Sorry, the requested resource does not exist",
            "internalMessage":"No car found in the database",
            "code":"4xx",
            "more info":"http://dev.example.com/api/v1/errors/12345"
        }
    ]
}
```

#####**9、返回结果（Response）**

服务器返回的数据格式，应该尽量使用JSON，避免使用XML。针对不同操作，服务器向用户返回的结果应该符合以下规范。
-  GET /collection：返回资源对象的列表（数组）
-  GET /collection/resource：返回单个资源对象
-  POST /collection：返回新生成的资源对象
-  PUT /collection/resource：返回完整的资源对象
-  PATCH /collection/resource：返回完整的资源对象
-  DELETE /collection/resource：返回一个空文档


#####**10、使用HATEOAS的Hypermedia API**

RESTful API最好使用Hypermedia as the Engine of Application State（超媒体作为应用状态的引擎），即返回结果中提供链接，连向其他API方法，超文本链接可以建立更好的文本浏览，使得用户不查文档，也知道下一步应该做什么。

比如，当用户向api.example.com的根目录发出请求，会得到这样一个文档。

```json
{
    "link":{
        "rel":"collection https://www.example.com/zoos",
        "href":"https://api.example.com/zoos",
        "title":"List of zoos",
        "type":"application/vnd.yourformat+json"
    }
}
```
上面代码表示，文档中有一个link属性，用户读取这个属性就知道下一步该调用什么API了。rel表示这个API与当前网址的关系（collection关系，并给出该collection的网址），href表示API的路径，title表示API的标题，type表示返回类型。

#####**11、认证（Authentication）**
API的身份认证尽量使用OAuth 2.0框架

###三、Swagger API标准  
API的文档管理和信息描述，将使用Swagger进行。  Swagger是一个规范和完整的框架，用于生成、描述、调用和可视化RESTful风格的Web服务。Swagger的目标是对REST API定义一个标准的和语言无关的接口，可让人和计算机无需访问源码、文档或网络流量监测就可以发现和理解服务的能力。 

Swagger规范定义了一组描述一个API所需的文件格式，类似于描述Web服务的WSDL。通过Swagger进行REST API的正确定义，用户可以理解远程服务并使用最少实现逻辑与远程服务进行交互。与为底层编程所实现的接口类似，Swagger消除了调用服务时可能会有的猜测。

注：Microsoft,PayPal等公司也已经引入Swagger 来定义自己的REST API 文档。  Swagger API可以使用YAML或JSON来表示。 Swagger这类API文档工具可以满足下列需求：
-  支持API自动生成同步的在线文档 
-  这些文档可用于项目内部API审核
-  方便测试人员了解API 
-  这些文档可作为客户产品文档的一部分进行发布 
-  支持API规范生成代码，生成的客户端和服务器端骨架代码可以加速开发和测试速度 

通常情况下，API的Swagger描述为JSON文件，也可使用YAML描述的文件。

**附Swagger文件示例：**

```json
{
    "swagger":"2.0",
    "info":{
        "version":"1.0.0",
        "title":"Swagger Petstore (Simple)",
        "description":"A sample API that uses a petstore as an example to demonstrate features in the swagger-2.0 specification",
        "termsOfService":"http://helloreverb.com/terms/",
        "contact":{
            "name":"Swagger API team",
            "email":"foo@example.com",
            "url":"http://swagger.io"
        },
        "license":{
            "name":"MIT",
            "url":"http://opensource.org/licenses/MIT"
        }
    },
    "host":"petstore.swagger.io",
    "basePath":"/api",
    "schemes":[
        "http"
    ],
    "consumes":[
        "application/json"
    ],
    "produces":[
        "application/json"
    ],
    "paths":{
        "/pets":{
            "get":{
                "description":"Returns all pets from the system that the user has access to",
                "operationId":"findPets",
                "produces":[
                    "application/json",
                    "application/xml",
                    "text/xml",
                    "text/html"
                ],
                "parameters":[
                    {
                        "name":"tags",
                        "in":"query",
                        "description":"tags to filter by",
                        "required":false,
                        "type":"array",
                        "items":{
                            "type":"string"
                        },
                        "collectionFormat":"csv"
                    },
                    {
                        "name":"limit",
                        "in":"query",
                        "description":"maximum number of results to return",
                        "required":false,
                        "type":"integer",
                        "format":"int32"
                    }
                ],
                "responses":{
                    "200":{
                        "description":"pet response",
                        "schema":{
                            "type":"array",
                            "items":{
                                "$ref":"#/definitions/pet"
                            }
                        }
                    },
                    "default":{
                        "description":"unexpected error",
                        "schema":{
                            "$ref":"#/definitions/errorModel"
                        }
                    }
                }
            },
            "post":{
                "description":"Creates a new pet in the store. Duplicates are allowed",
                "operationId":"addPet",
                "produces":[
                    "application/json"
                ],
                "parameters":[
                    {
                        "name":"pet",
                        "in":"body",
                        "description":"Pet to add to the store",
                        "required":true,
                        "schema":{
                            "$ref":"#/definitions/newPet"
                        }
                    }
                ],
                "responses":{
                    "200":{
                        "description":"pet response",
                        "schema":{
                            "$ref":"#/definitions/pet"
                        }
                    },
                    "default":{
                        "description":"unexpected error",
                        "schema":{
                            "$ref":"#/definitions/errorModel"
                        }
                    }
                }
            }
        },
        "/pets/{id}":{
            "get":{
                "description":"Returns a user based on a single ID, if the user does not have access to the pet",
                "operationId":"findPetById",
                "produces":[
                    "application/json",
                    "application/xml",
                    "text/xml",
                    "text/html"
                ],
                "parameters":[
                    {
                        "name":"id",
                        "in":"path",
                        "description":"ID of pet to fetch",
                        "required":true,
                        "type":"integer",
                        "format":"int64"
                    }
                ],
                "responses":{
                    "200":{
                        "description":"pet response",
                        "schema":{
                            "$ref":"#/definitions/pet"
                        }
                    },
                    "default":{
                        "description":"unexpected error",
                        "schema":{
                            "$ref":"#/definitions/errorModel"
                        }
                    }
                }
            },
            "delete":{
                "description":"deletes a single pet based on the ID supplied",
                "operationId":"deletePet",
                "parameters":[
                    {
                        "name":"id",
                        "in":"path",
                        "description":"ID of pet to delete",
                        "required":true,
                        "type":"integer",
                        "format":"int64"
                    }
                ],
                "responses":{
                    "204":{
                        "description":"pet deleted"
                    },
                    "default":{
                        "description":"unexpected error",
                        "schema":{
                            "$ref":"#/definitions/errorModel"
                        }
                    }
                }
            }
        }
    },
    "definitions":{
        "pet":{
            "type":"object",
            "required":[
                "id",
                "name"
            ],
            "properties":{
                "id":{
                    "type":"integer",
                    "format":"int64"
                },
                "name":{
                    "type":"string"
                },
                "tag":{
                    "type":"string"
                }
            }
        },
        "newPet":{
            "type":"object",
            "required":[
                "name"
            ],
            "properties":{
                "id":{
                    "type":"integer",
                    "format":"int64"
                },
                "name":{
                    "type":"string"
                },
                "tag":{
                    "type":"string"
                }
            }
        },
        "errorModel":{
            "type":"object",
            "required":[
                "code",
                "message"
            ],
            "properties":{
                "code":{
                    "type":"integer",
                    "format":"int32"
                },
                "message":{
                    "type":"string"
                }
            }
        }
    }
}
```



