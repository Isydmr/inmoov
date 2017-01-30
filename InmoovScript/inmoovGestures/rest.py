# ##############################################################################
# 				ROBOT REST POSITIONS ( minimal )
# ##############################################################################

def rest():
	fullspeed()
	if isRightHandActivated:
		i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
		i01.rightHand.rest()
	
	if isLeftHandActivated:
		i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
		i01.leftHand.rest()
	
	if isRightArmActivated:
		i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
		i01.rightArm.rest()
	
	if isLeftArmActivated:
		i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
		i01.leftArm.rest()
		
# ##############################################################################
# 				ROBOT REST POSITIONS ( full )
# ##############################################################################		
	
	if isHeadActivated:
		i01.setHeadSpeed(1.0, 1.0)
		i01.head.rest()
	
	if isTorsoActivated:
		i01.setTorsoSpeed(1.0, 1.0, 1.0)
		i01.torso.rest()
	
	if isRollNeckActivated:
		i01.setSpeed(1.0)
		rollneck.rest()

		
		
# ##############################################################################
# 				full speed
# ##############################################################################
		
def fullspeed():
	if isRightHandActivated:
		i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
			
	if isLeftHandActivated:
		i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
			
	if isRightArmActivated:
		i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
		
	if isLeftArmActivated:
		i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
	
	if isHeadActivated:
		i01.setHeadSpeed(1.0, 1.0)
	
	if isTorsoActivated:
		i01.setTorsoSpeed(1.0, 1.0, 1.0)
			
	if isRollNeckActivated:
		i01.setSpeed(1.0)
		
   #TODO RANDOM GESTURE
   #global MoveBodyRandom
   #MoveBodyRandom=0
   #global MoveHeadRandom
   #MoveHeadRandom=0