"""parse module"""
from dataclasses import dataclass
from typing import Tuple, Set, List


@dataclass
class Location:
    """Location coodinates for tile"""
    map_coordinates: Tuple[int, int]
    tile_row: int
    tile_column: int


@dataclass
class MapPlots:
    """Walkable Garden Plots"""
    start_location: Tuple[int, int]
    map_plots: Set[Tuple[int, int]]
    total_rows: int
    total_columns: int

    def get_neighbors(
        self,
        original_coords: Tuple[int, int],
        is_tiled: bool,
        traveled: Set[Tuple[int, int]],
    ) -> List[Tuple[int, int]]:
        """Returns all walkable neighbours

        Args:
            original_coords (Tuple[int, int]): coodinate to search from
            is_tiled (bool): if True, map is becomes a "tile" in an infinite garden
            traveled (Set[Tuple[int, int]]): coodinates that have already been visited
                                             and we do not want to travel again

        Returns:
            List[Tuple[int, int]]: list of coodinates to return
        """
        neighbors = []

        up_coord = (original_coords[0]-1, original_coords[1])
        if up_coord not in traveled and self.exists(up_coord, is_tiled):
            neighbors.append(up_coord)

        left_coord = (original_coords[0], original_coords[1] - 1)
        if left_coord not in traveled and self.exists(left_coord, is_tiled):
            neighbors.append(left_coord)

        right_coord = (original_coords[0], original_coords[1] + 1)
        if right_coord not in traveled and self.exists(right_coord, is_tiled):
            neighbors.append(right_coord)

        down_coord = (original_coords[0]+1, original_coords[1])
        if down_coord not in traveled and self.exists(down_coord, is_tiled):
            neighbors.append(down_coord)

        return neighbors

    def exists(self, coodinates: Tuple[int, int], is_tiled: bool) -> Location | None:
        """checks if coodinates exists in mapping

        Args:
            coodinates (Tuple[int, int]): coodinates to test if it exists in mapping
            is_tiled (bool): if True, map is becomes a "tile" in an infinite garden

        Returns:
            Location | None: Returns a location if found
        """
        tile_row = 0
        tile_column = 0
        if is_tiled:
            # get non-infinite location
            tile_row = coodinates[0] // self.total_rows
            tile_column = coodinates[1] // self.total_columns
            non_inifinite_row = coodinates[0] % self.total_rows
            non_inifinite_column = coodinates[1] % self.total_columns
            coodinates = (non_inifinite_row, non_inifinite_column)

        if coodinates in self.map_plots:
            return Location(
                coodinates,
                tile_row,
                tile_column,
            )

        return None


def parse_input(input_file: str) -> MapPlots:
    """parses input file into a MapPlots object

    Args:
        input_file (str): input file

    Returns:
        MapPlots: Mapping of all walkable locations
    """

    start_location = None
    map_plots = set()
    total_rows = 0
    total_columns = 0
    with open(input_file, encoding="utf-8") as file_input:

        for row, line in enumerate(file_input):
            total_rows = max(row, total_rows)
            for column, character in enumerate(line.strip()):
                total_columns = max(column, total_columns)
                location = (row, column)

                if character == "#":
                    continue

                if character == "S":
                    start_location = location

                map_plots.add(location)

    return MapPlots(start_location, map_plots, total_rows + 1, total_columns + 1)
