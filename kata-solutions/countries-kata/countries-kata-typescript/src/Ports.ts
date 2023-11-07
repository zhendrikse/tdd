import { Country} from "./Country";

export interface InputPort {
  load_all(): Country[];
}

export interface OutputPort {
  write(data: string[][]): void;
}