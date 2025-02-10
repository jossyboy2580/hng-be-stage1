# A submission for the HNG12 Stage 1 task 

This api takes in a number and returns some information about the number

### endpoint
/api/classify-number?number=<number>

### response
#### on success
example
- {
'number': 371,
'is_prime': false,
'is_perfect': false,
'properties': ['armstrong', 'odd'],
'digit_sum': 11,
'fun_fact': '371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371'
}

### on error
example
- {
'number': 'alphabet',
'error': true
}
