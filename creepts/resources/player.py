import falcon
import json
import logging
from .. import constants as const
from ..utils import blockchain_utils as bc_utils

LOGGER = logging

class Player:
    def on_get(self, req, resp):
        """
        Handles the get method for Player resource

        Parameters
        ----------
        req : falcon.Request
            Contains the request, this method has no input parameters

        resp: falcon.Response
            This object is used to issue the response to this call it,
            if no error occurs, it should return a json structure describing the
            player information. Currently it consist of the player address

        Returns
        -------
        NoneType
            This method has no return
        """

        LOGGER.info("Get player")
        address = const.PLAYER_OWN_ADD
        balance = 0

        try:
            balance = bc_utils.get_player_balance(address)
        except Exception as e:
            # let's just log the exception and return a zero balance, so it works without the blockchain
            LOGGER.exception(e)

        resp.body = json.dumps({ "address": address, "balance": balance })
        resp.status = falcon.HTTP_200
