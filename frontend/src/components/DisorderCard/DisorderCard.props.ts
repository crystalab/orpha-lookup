import { DisorderInstance } from '../../mobx/models/Disorder';

export interface DisorderCardProps {
  disorder: DisorderInstance;
  selectedHpoIds: object;
}
