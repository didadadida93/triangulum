from typing import Union, Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.enums import CelebrationType, BuildingType, RomanUnit, TeutonUnit, GaulUnit
from triangulum.utils.dataclasses import RomanUnits, TeutonUnits, GaulUnits


class Building(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='building')

    def get_celebration_list(self, village_id: int, location_id: int) -> dict:
        """Get list of running celebrations in a village

        Args:
            village_id: ID of the village
            location_id: ID of the location of the Town Hall

        Returns:
            dict
        """
        return self.invoke_action(
            action='getCelebrationList',
            params={
                'villageId': village_id,
                'locationId': location_id,
            }
        )

    def start_celebration(self, village_id: int, celebration_type: CelebrationType) -> dict:
        """Start a celebration

        Args:
            village_id: ID of the village
            celebration_type: Type of the celebration

        Returns:
            dict
        """
        return self.invoke_action(
            action='startCelebration',
            params={
                'villageId': village_id,
                'type': celebration_type.value,
            }
        )

    def get_building_list(self, village_id: int, location_id: int) -> dict:
        """Get information on a building at a particular location_id or the
        list of buildings that can be built in that spot

        Args:
            village_id: ID of the village
            location_id: ID of the location

        Returns:
            dict
        """
        return self.invoke_action(
            action='getBuildingList',
            params={
                'villageId': village_id,
                'locationId': location_id,
            }
        )

    def get_trapper_infos(self, village_id: int, location_id: int) -> dict:
        """Get information about a trapper

        Args:
            village_id: ID of the village
            location_id: ID of the location

        Returns:
            dict
        """
        return self.invoke_action(
            action='getTrapperInfos',
            params={
                'villageId': village_id,
                'locationId': location_id,
            }
        )

    def build_traps(self, village_id: int, location_id: int, amount: int) -> dict:
        """Build traps in a trapper

        Args:
            village_id: ID of the village
            location_id: ID of the trapper location
            amount: Amount of traps to be built

        Returns:
            dict
        """
        return self.invoke_action(
            action='buildTraps',
            params={
                'villageId': village_id,
                'locationId': location_id,
                'amount': amount,
            }
        )

    def upgrade(self, village_id: int, location_id: int, building_type: BuildingType) -> dict:
        """Upgrade a building

        Args:
            village_id: ID of the village
            location_id: ID of the building location
            building_type: Type of the building

        Returns:
            dict
        """
        return self.invoke_action(
            action='upgrade',
            params={
                'villageId': village_id,
                'locationId': location_id,
                'buildingType': building_type.value,
            }
        )

    def get_recruit_list(self, village_id: int, location_id: int) -> dict:
        """Get list of units currently in the recruitment queue

        Args:
            village_id: ID of the village
            location_id: ID of the recruitment building (i.e barracks, stable, workshop) location

        Returns:
            dict
        """
        return self.invoke_action(
            action='getRecruitList',
            params={
                'villageId': village_id,
                'locationId': location_id,
            }
        )

    def recruit_units(
            self,
            village_id: int,
            location_id: int,
            units: Union[RomanUnits, TeutonUnits, GaulUnits]
    ) -> dict:
        """Recruit new units

        Args:
            village_id: ID of the village
            location_id: ID of the recruitment building (i.e barracks, stable, workshop) location
            units: Collection of units to be recruited

        Returns:
            dict
        """
        return self.invoke_action(
            action='recruitUnits',
            params={
                'villageId': village_id,
                'locationId': location_id,
                'units': units.without_zeros(),
            }
        )

    def use_master_builder(
        self,
        village_id: int,
        location_id: int,
        building_type: BuildingType,
        reserve_resources: bool,
        count: int = 1
    ) -> dict:
        """Use master builder to finish a task early, queue a task
        or reserve the resources for a task

        Args:
            village_id: ID of the village
            location_id: ID of the building location
            building_type: Type of the building
            reserve_resources: Whether to reserve resources for the task
            count: Count of tasks to reserve (appears to be hardcoded as 1 by the API)

        Returns:
            dict
        """
        return self.invoke_action(
            action='useMasterBuilder',
            params={
                'villageId': village_id,
                'locationId': location_id,
                'buildingType': building_type.value,
                'reserveResources': reserve_resources,
                'count': count
            }
        )

    def get_oasis_list(self, village_id: int) -> dict:
        """Get a list of oasis within the influence range of a village

        Args:
            village_id: ID of the village

        Returns:
            dict
        """
        return self.invoke_action(
            action='getOasisList',
            params={
                'villageId': village_id,
            }
        )

    def get_culture_point_balance(self, village_id: int) -> dict:
        """Retrieve the culture point balance

        Args:
            village_id: ID of the village

        Returns:
            dict
        """
        return self.invoke_action(
            action='getCulturePointBalance',
            params={
                'villageId': village_id,
            }
        )

    def reserve_resources(self, village_id: int, entry_id: int) -> dict:
        """Reserve resources for a master builder task

        Args:
            village_id: ID of the village
            entry_id: Master builder entry ID

        Returns:
            dict
        """
        return self.invoke_action(
            action='reserveResources',
            params={
                'villageId': village_id,
                'entryId': entry_id,
            }
        )

    def cancel(self, village_id: int, event_id: int) -> dict:
        """Cancel an event

        Args:
            village_id: ID of the village
            event_id: ID of the event

        Returns:

        """
        return self.invoke_action(
            action='cancel',
            params={
                'villageId': village_id,
                'eventId': event_id,
            }
        )

    def research_unit(
        self,
        village_id: int,
        location_id: int,
        building_type: BuildingType,
        unit_type: Union[RomanUnit, TeutonUnit, GaulUnit]
    ) -> dict:
        """Research a unit either in the smithy or the academy

        Args:
            village_id: ID of the village
            location_id: ID of the research building location
            building_type: Type of the research building
            unit_type: Type of the unit

        Returns:
            dict
        """
        return self.invoke_action(
            action='researchUnit',
            params={
                'villageId': village_id,
                'locationId': location_id,
                'buildingType': building_type.value,
                'unitType': unit_type.value,
            }
        )

    def shift_master_builder(self, village_id: int, shift_from: int, shift_to: int) -> dict:
        """Shift the positions of a master builder reservation

        Args:
            village_id: ID of the village
            shift_from: Current position in the master builder reservation queue
            shift_to: Desired position in the master builder reservation queue

        Returns:
            dict
        """
        return self.invoke_action(
            action='shiftMasterBuilder',
            params={
                'villageId': village_id,
                'from': shift_from,
                'to': shift_to
            }
        )

    def destroy(self, village_id: int, location_id: int) -> dict:
        """Begin a destruction task of a building in your village

        Args:
            village_id: ID of the village
            location_id: ID of the building location

        Returns:
            dict
        """
        return self.invoke_action(
            action='destroy',
            params={
                'villageId': village_id,
                'locationId': location_id
            }
        )

    def get_treasury_transformations(self) -> dict:
        """Get information on treasury transformations in your gameworld account

        Returns:
            dict
        """
        return self.invoke_action(
            action='getTreasuryTransformations'
        )

    def transform_treasury(self, village_id: int, location_id: int) -> dict:
        """Begin a treasury transformation task

        Args:
            village_id: ID of the village the treasury is located in
            location_id: ID of the treasury building location

        Returns:
            dict
        """
        return self.invoke_action(
            action='transformTreasury',
            params={
                'villageId': village_id,
                'locationId': location_id,
            }
        )

    def get_cp_data(self, village_id: int) -> dict:
        """Get culture point data

        Args:
            village_id: ID of a village

        Returns:
            dict
        """
        return self.invoke_action(
            action='getCpData',
            params={
                'villageId': village_id,
            }
        )
