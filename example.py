import gym
env = gym.make('CartPole-v0')
sum = 0
runs = 0
right = True
second = False
oldV = 0
a = 0
velocity = 0
success = 0
jerk = 0
oldA = 0
for i_episode in range(10):
    first = True
    observation = env.reset()
    for t in range(200):
        env.render()
        print(observation)
        angVelocity = observation[3]
        velocity = observation[1]
        # if(first and velocity < 0):
        #     action = 0
        #     first = False
        # elif(first and velocity >0):
        #     action = 1
        #     first = False

        if(first):
            action = 0
            first = False
        # elif(angVelocity>-.1 and angVelocity<.1):
        #     if(right and not second):
        #         action = 1
        #         right = True
        #         second = True
        #     elif(right and second):
        #         action = 1
        #         right = False
        #         second = False
        #     elif(not right and not second):
        #         action = 0
        #         right = False
        #         second = True
        #     else:
        #         action = 0
        #         right = True
        #         second = False
        elif(angVelocity>-.1 and angVelocity<.1):
            if(right):
                action = 1
                right = False
            else:
                action = 0
                right = True
        else:
            if(angVelocity>.1):
                action = 1
            elif(angVelocity<-.1):
                action = 0

        # if(jerk>1):
        #     action = 0
        # elif(jerk<-1):
        #     action = 1

        # if(not a>.01 and not a<-.01 and not angVelocity>.01 and not angVelocity<-.01 and right):
        #     action = 0
        # elif(not a>.01 and not a<-.01 and not angVelocity>.01 and not angVelocity<-.01 and not right):
        #     action = 1


        #i = input("Right or Left?")

        if(action ==1):
            print("right")
            right=True
        else:
            print("left")
            right=False
        a+=(velocity - oldV)
        jerk +=(a-oldA)
        print(a)
        print(t+1)
        if(t+1>199):
            success+=1
        oldV = velocity
        oldA = a
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            sum += t+1
            runs +=1
            break
print(sum/runs)
print(success)
