class Odometry:

    def __init__(self):
        self.position = self.InitPosition()
        self.orientation = self.InitOrientation()

    class InitPosition:
        def __init__(self, values = (0, 0, 0)):
            self.x, self.y, self.z = values

    class InitOrientation:
        def __init__(self, values = (0, 0, 0, 0)):
            self.x, self.y, self.z, self.w = values

    def __str__(self):
        outstr = '\n'.join(['Position: ({:.4f}, {:.4f}, {:.4f})'.format(
                    self.position.x, self.position.y, self.position.z),
                'Orientation: ({:.4f}, {:.4f}, {:.4f}, {:.4f})'.format(
                    self.orientation.x, self.orientation.y, self.orientation.z,
                    self.orientation.w)])
        return outstr

def delta(start_odom, start_RPY, end_odom, end_RPY):
    import pandas as pd
    pd.set_option("display.precision", 3,
              "display.float_format", '{:0.2f}'.format)

    df = pd.DataFrame({'start': [start_odom.position.x,
                        start_odom.position.y, start_odom.position.z,
                        start_RPY[0],start_RPY[1],start_RPY[2]],
                       'end': [end_odom.position.x,
                        end_odom.position.y, end_odom.position.z,
                        end_RPY[0],end_RPY[1],end_RPY[2]]},
                 index = ['linear_x','linear_y','linear_z',
                          'theta_x(Roll)','theta_y(Pitch)','theta_z(Yaw)'])

    df['delta'] = df['end'] - df['start']
    df = df[['start', 'end', 'delta']]

    return df
