import modal

stub = modal.Stub("wl-example")

@stub.function()
def multiply_two_ints_and_return_msg(int1, int2):
    product_of_ints = int1 * int2
    msg = "Whooo this worked!"
    print (msg, product_of_ints)
    return msg, product_of_ints


#if __name__ == "__main__":
@stub.local_entrypoint()
def main():

    # run the function locally
    multiply_two_ints_and_return_msg.local(12,3)

    # run the function remotely on Modal
    multiply_two_ints_and_return_msg.remote(12,3)

    # run the function in parallel and remotely on Modal
    total = 0
    for msg, ret in multiply_two_ints_and_return_msg.map(range(20), range(20)):
        total += ret

    print("total of all products:", total)