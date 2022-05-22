def Factory(max):
    def add(callback):
        def run(origin):
            sum = 0
            for i in range(1, max+1):
                sum+=i
            callback(sum+origin)
        return run
    return add

@Factory(100)
def show(result):
    print(result)

show(10)
