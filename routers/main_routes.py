from fastapi import APIRouter, status
from controllers import movement_controllers

router = APIRouter(
    tags=['Controls'],
    prefix='/car'
)

router.add_api_route('/left',movement_controllers.left,methods=['GET'])

router.add_api_route('/right',movement_controllers.right,methods=['GET'])

router.add_api_route('/forward',movement_controllers.forward,methods=['GET'])

router.add_api_route('/stop',movement_controllers.stop,methods=['GET'])






