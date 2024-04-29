import math
from mavsdk import System

async def run():
    # Connect to the AirSim simulator
    drone = System()
    await drone.connect()
    status_text_task = asyncio.ensure_future(print_status_text(drone))

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    # Wait for the drone to be ready
    await drone.action.arm()
    # await drone.action.set_takeoff_altitude(50)
    await drone.action.takeoff()

    await asyncio.sleep(20)

    ## Spiral flight pattern
    # Set the initial position
    start_position = None
    async for position in drone.telemetry.position():
        start_position = position
        start_lat = start_position.latitude_deg
        start_lon = start_position.longitude_deg
        start_altitude = start_position.absolute_altitude_m
        break

    print("start lat: ", start_lat, "start_lon: ", start_lon)

    # Convert to radians
    start_lat_rad = math.radians(start_lat)
    start_lon_rad = math.radians(start_lon)

    # Set the spiral parameters
    a = 1
    radius = 1
    target_radius = 5
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
        # print("radius: ", radius, "target_radius: ", target_radius, "theta: ", theta)
        print("lat: ", math.degrees(curr_lat), "lon: ", math.degrees(curr_lon))

        await asyncio.sleep(10)

        # Increase the radius for the next loop
        theta += 0.1
       
    # Land the drone
    await drone.action.land()

async def print_status_text(drone):
    try:
        async for status_text in drone.telemetry.status_text():
            print(f"Status: {status_text.type}: {status_text.text}")
    except asyncio.CancelledError:
        return

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())
