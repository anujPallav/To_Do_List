TO_DO_LIST_CONTAINER = []
LOOP_BOOL = None

def get_finalized():
    print('................................................Hurry! your list is empty..............................................')

def get_task_in_list():
    def list_manager(get_user_auth):
        get_user_input = input('Enter a task: ')
        TO_DO_LIST_CONTAINER.append(get_user_input)
        get_user_auth()
        
    def get_user_auth():
        user_input = input('continue y/n?: ')
        if user_input == 'y':
            list_manager(get_user_auth)
        elif user_input == 'n':
            print('\n')
            print('Your To-Do-List is:\n')
            count = len(TO_DO_LIST_CONTAINER)
            for i in range(0,count):
                print(f'{i}-{TO_DO_LIST_CONTAINER[i]}')
        else:
            print('Invalid Input')
            get_user_auth()

    def get_clean_list(update_list):
        print('\n')
        print('For removing task enter index number \n')
        global LOOP_BOOL
        LOOP_BOOL = True
        while LOOP_BOOL:
            try:
                get_index_number = int(input('Enter a index number: '))
                TO_DO_LIST_CONTAINER.pop(get_index_number)
                update_list()
                count_remain = len(TO_DO_LIST_CONTAINER)    
                if count_remain == 0:
                    LOOP_BOOL = False
                    get_finalized()
            except:
                print('........................................Somethig Went Wrongy.......................................')
                  
                get_clean_list(update_list)

    def update_list():              
        count_remain = len(TO_DO_LIST_CONTAINER)        
        for i in range(0,count_remain):
            print(f'{i}-{TO_DO_LIST_CONTAINER[i]}')
    list_manager(get_user_auth)
    get_clean_list(update_list)

get_task_in_list()
