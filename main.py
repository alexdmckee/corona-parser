from gateway.worldometer_gateway import WorldOMeterGateway
from services.parser_service import ParserService

if __name__ == "__main__":

    worldometer_gateway = WorldOMeterGateway()
    parser_service = ParserService()

    latest_world_data = worldometer_gateway.fetch("world")
    latest_states_data = worldometer_gateway.fetch("states")
    outputWorld = parser_service.create_df_worldometer(latest_world_data, "world")
    outputUSAStates = parser_service.create_df_worldometer(latest_states_data, "states")
    last_updated = parser_service.parse_last_updated(latest_world_data)

    outputWorld.to_csv(r'./worldCases.csv', index=False)
    outputWorld.set_index("Country/Other").to_json(r"./worldCases.json", orient="index", indent = 2)
    outputUSAStates.to_csv(r'./USAStatesCases.csv', index=False)
    outputUSAStates.set_index("USA State").to_json(r"./USAStatesCases.json", orient="index", indent=2)
    print(last_updated)
    print(outputWorld)
