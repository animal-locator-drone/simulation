import math
from mavsdk import System

async def run():
    # Connect to the AirSim simulator
    drone = System()
    await drone.connect()

    print("Waiting for drone to connect...")
    # async for state in drone.core.connection_state():
    #     if state.is_connected:
    #         print(f"-- Connected to drone!")
    #         break

    # Wait for the drone to be ready
    await drone.action.arm()
    # await drone.action.set_takeoff_altitude(50)
    await drone.action.takeoff()

    # await asyncio.sleep(20)

    ## Spiral flight pattern
    # Set the initial position
    start_position = None
    async for position in drone.telemetry.position():
        start_position = position
        start_lat = start_position.latitude_deg
        start_lon = start_position.longitude_deg
        start_altitude = start_position.absolute_altitude_m
        break

    # Convert to radians
    start_lat_rad = math.radians(start_lat)
    start_lon_rad = math.radians(start_lon)

    # Set the spiral parameters
    a = 1
    radius = 1
    target_radius = 50
    theta = math.atan2(start_lat_rad, start_lon_rad)

    # Fly the spiral pattern
    while radius < target_radius:
        # Calculate the current position on the spiral
        radius = a * theta
        curr_lat = radius * math.cos(theta)
        curr_lon = radius * math.sin(theta)

        # Move the drone to the current position
        await drone.action.goto_location(
            latitude_deg=math.degrees(curr_lat),
            longitude_deg=math.degrees(curr_lon), 
            absolute_altitude_m=start_altitude,
            yaw_deg=0)

        # Increase the radius for the next loop
        theta += 5
        
    # Land the drone
    await drone.action.land()

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())