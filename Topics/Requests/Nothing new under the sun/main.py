# from flask import Flask
# from flask import request

# app = Flask('main')

# @app.route('/', methods=['DELETE', 'PUT', 'GET'])
def database_manipulator():
    # if request.method == 'GET':
    #     template = """
    #     <form method='PUT'>
    #     <input type='submit' value='PUT'>
    #     </form>
        
    #     <form method='DELETE'>
    #     <input type='submit' value='DELETE'>
    #     </form>
    #     """
        # return template
    if request.method == 'DELETE':
        return 'Deleted'
    elif request.method == 'PUT':
        return 'Updated'
