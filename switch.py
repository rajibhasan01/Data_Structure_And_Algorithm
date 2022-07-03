def number_to_string(argument):
    match argument:
            case 0:
                return 'Zero';
            case 1:
                return 'One';
            case 2:
                return 'Two';
            case default:
                return 'something';

if __name__ == "__mani__":
    argument = 0;
    number_to_string(argument);
