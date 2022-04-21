from random import randint


def lambda_handler(event, context):
    
    print('Processing')
    #Our ETL code to process the file would go here
    value = randint(0, 1)
    # We now divide 10 by our random number.
    # If the random number is 0, our function will fail
    newval = 10 / value
    print(f'New Value is: {newval}')
    return (newval)