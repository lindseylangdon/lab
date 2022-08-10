class Television:
    '''
    A class representing details for a television object
    '''
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        '''
        Constructor to create intial state of a television object
        '''
        self.__tv_channel = Television.MIN_CHANNEL
        self.__tv_volume = Television.MIN_VOLUME
        self.__tv_status = False

    def power(self) -> None:
        '''
        Method to turn the television on and off
        '''
        if self.__tv_status == False:
            self.__tv_status = True
        else:
            self.__tv_status = False

    def channel_up(self) -> None:
        '''
        Method to increase television channel
        '''
        if self.__tv_status == True:
            if self.__tv_channel < Television.MAX_CHANNEL:
                self.__tv_channel += 1
            else:
                self.__tv_channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        Method to decrease televsion channel
        '''
        if self.__tv_status == True:
            if self.__tv_channel > Television.MIN_CHANNEL:
                self.__tv_channel =- 1
            else:
                self.__tv_channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        Method to increase television volume
        '''
        if self.__tv_status == True:
            if self.__tv_volume < Television.MAX_VOLUME:
                self.__tv_volume += 1
            else:
                self.__tv_volume = Television.MAX_VOLUME
                       

    def volume_down(self) -> None:
        '''
        Method to decrease television volume
        '''
        if self.__tv_status == True:
            if self.__tv_volume > Television.MIN_VOLUME:
                self.__tv_volume -= 1
            else:
                self.__tv_volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        '''
        Method that returns the TV status
        :return: TV status
        '''
        return f'TV status: Is on = {self.__tv_status}, Channel = {self.__tv_channel}, Volume = {self.__tv_volume}'
