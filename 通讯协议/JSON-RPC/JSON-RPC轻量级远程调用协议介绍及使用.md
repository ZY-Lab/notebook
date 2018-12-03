## JSON-RPC轻量级远程调用协议介绍及使用

###技术简介
json-rpc是基于json的跨语言远程调用协议，比xml-rpc、webservice等基于文本的协议传输数据格小；相对hessian、Java-rpc等二进制协议便于调试、实现、扩展，是非常优秀的一种远程调用协议。目前主流语言都已有json-rpc的实现框架，java语言中较好的json-rpc实现框架有jsonrpc4j、jpoxy、json-rpc。三者之中jsonrpc4j既可独立使用，又可与spring无缝集合，比较适合于基于spring的项目开发。

####一、JSON-RPC协议描述
json-rpc协议非常简单，发起远程调用时向服务端传输数据格式如下：
>{ "method": "sayHello", "params": ["Hello JSON-RPC"], "id": 1}
#####参数说明：
method： 调用的方法名
params： 方法传入的参数，若无参数则传入 []
id ： 调用标识符，用于标示一次远程调用过程

服务器其收到调用请求，处理方法调用，将方法效用结果效应给调用方；返回数据格式：
>{
    "result":          "Hello JSON-RPC",
    "error":                null,
      "id":                      1
 }
#####参数说明:
result: 方法返回值，若无返回值，则返回null。若调用错误，返回null。
error ：调用时错误，无错误返回null。
id : 调用标识符，与调用方传入的标识符一致。
以上就是json-rpc协议规范，非常简单，小巧，便于各种语言实现。

####二、JSON-RPC简单示例
#####2.1、服务器端Java调用示例
jsonrpc4j服务器端java示例：
>public class HelloWorldServlet extends HttpServlet {
    private static final long serialVersionUID = 3638336826344504848L;
    private JsonRpcServer rpcService = null;
    @Override
    public void init(ServletConfig config) throws ServletException {
        super.init(config);
        rpcService = new JsonRpcServer(new HelloWorldService(), HelloWorldService.class);
    }
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        rpcService.handle(req, resp);    
    }
}

#####2.2、Java客户端调用示例
jsonrpc4j的Java客户端调用示例：
>JsonRpcHttpClient client = new JsonRpcHttpClient(
new URL("http://127.0.0.1:8080/index.json"));
Map<String,String> headers = new HashMap<String,String>();
headers.put("name", "剑白");
client.setHeaders(headers);
String properties = client.invoke("getSystemProperties", null, String.class);
System.out.println(properties);

#####2.3、PHP客户端调用示例
基于json-rpc-PHP的php客户端调用示例：
><?php include(dirname(__FILE__)."/lib/client/JsonRpcClient.php");
$client = new JsonRpcClient("http://10.13.49.234:8080/index.json");
$response = $client->getSystemProperties();
echo $response->result;
?>

#####2.3、JavaScript客户端调用示例
基于jsonrpcjs的JavaScript客户端调用示例：
>var rpc = new jsonrpc.JsonRpc('http://127.0.0.1:8080/index.json');
rpc.call('getSystemProperties', function(result){
alert(result);
});

#####2.4、直接GET请求进行调用
无需任何客户端，只需手工拼接参数进行远程调用，请求URL如下：
http://127.0.0.1:8080/index.json?method=getSystemProperties&id=3325235235235&params=JTViJTVk
参数说明:
method : 方法名
params ：调用参数，json的数组格式[], 将参数需先进行url编码，再进行base64编码
id : 调用标识符，任意值。
####三、JSON-RPC总结
json-rpc是一种非常轻量级的跨语言远程调用协议，实现及使用简单。仅需几十行代码，即可实现一个远程调用的客户端，方便语言扩展客户端的实现。服务器端有php、java、Python、ruby、.net等语言实现，是非常不错的及轻量级的远程调用协议。
参考文档
http://code.google.com/p/jsonrpc4j/
http://json-rpc.org/wiki/implementations
http://en.wikipedia.org/wiki/JSON-RPC
https://github.com/gimmi/jsonrpcjs
http://bitbucket.org/jbg/php-json-rpc
https://github.com/Pozo/json-rpc-php
https://github.com/subutux/json-rpc2php