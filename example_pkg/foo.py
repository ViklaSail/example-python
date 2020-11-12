import awesome

def foo_func():
    print("this is a foo function")
    return "foo"

def laughingChain():
    return awesome.laughing() + awesome.laughing()

def laughingChainPara():
    return awesome.laughingPara("terse")

def funcSameNameSpace():
    return foo_func()