## General Notes: 


To deploy your app, you have to name it something like this 
`stub = modal.Stub("silly-example")`

You can add secrets on the website, or you can do it programmatically. Then, you can access them in your functions like this:
```
@stub.function(secrets=[modal.Secret.from_name("my-secret")]) 
def f():
    print(os.environ["MY_SECRET"]) 
```


You can also use starmap if you have more complex functions you want to parallelize
```
@stub.function()
def my_func(a, b):
    return a + b

@stub.local_entrypoint()
def main():
    assert list(my_func.starmap([(1, 2), (3, 4)])) == [3, 7]
```


You can also specify to use gpus:
`@stub.function(gpu="A10G")` -> specify gpu
`@stub.function(gpu="any")` -> if you're not picky
`@stub.function(gpu=modal.gpu.H100(count=8))` -> specify number of gpus
    
and you can request more cpu cores
`@stub.function(cpu=8.0)` -> specify number of cores


### Running an app
You can create temporary apps (like in these examples) by running `modal run <file>`. This will create an app that exists while your script is running. 

If you want to create an app that you can keep active (like a webpage endpoint), you can deploy it by `modal deploy <file>` or `modal serve <file>`

Once your app is deployed, you can hit it like this:
```
import modal
f = modal.Function.lookup("my-shared-app", "function-name")
f.remote(input)
```

You can make web endpoints by adding the 
`@web_endpoint()` decorator. Read more about this (here)[https://modal.com/docs/guide/webhooks]

