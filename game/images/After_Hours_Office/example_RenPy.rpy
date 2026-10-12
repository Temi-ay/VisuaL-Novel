# Shyvirelle: After Hours Office — optional integration example.
## Copy pack images/ to game/images/shy_office/
## Copy this file to game/ and call shy_office_demo from an existing label.

image shy_office reception_day = Transform("images/shy_office/reception_day.png", xysize=(config.screen_width, config.screen_height))
image shy_office reception_night = Transform("images/shy_office/reception_night.png", xysize=(config.screen_width, config.screen_height))
image shy_office meeting_day = Transform("images/shy_office/meeting_day.png", xysize=(config.screen_width, config.screen_height))
image shy_office meeting_night = Transform("images/shy_office/meeting_night.png", xysize=(config.screen_width, config.screen_height))
image shy_office manager_day = Transform("images/shy_office/manager_day.png", xysize=(config.screen_width, config.screen_height))
image shy_office manager_night = Transform("images/shy_office/manager_night.png", xysize=(config.screen_width, config.screen_height))

label shy_office_demo:
    scene shy_office reception_day
    with dissolve
    "Reception — day. Background preview."
    scene shy_office reception_night
    with dissolve
    "Reception — night. Background preview."
    scene shy_office meeting_day
    with dissolve
    "Meeting room — day. Background preview."
    scene shy_office meeting_night
    with dissolve
    "Meeting room — night. Background preview."
    scene shy_office manager_day
    with dissolve
    "Manager office — day. Background preview."
    scene shy_office manager_night
    with dissolve
    "Manager office — night. Background preview."
    return
