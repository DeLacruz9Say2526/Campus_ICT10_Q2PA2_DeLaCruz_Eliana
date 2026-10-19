from pyscript import document, display


def name(event):

    first_name = document.getElementById("fname")
    last_name = document.getElementById("surname")
    new_member = str(last_name) + str(first_name)
    add_mem = new_member

    members = {'Eliana De La Cruz', 'Princess Sagum', 'Joshua Santos'}
    members.add(add_mem)

    display(f'{members}', target='result', append=False)

    display(f'total number of members: {len(members)}', target='result')



