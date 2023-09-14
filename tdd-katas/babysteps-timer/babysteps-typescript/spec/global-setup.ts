import jsdomGlobal from 'jsdom-global';

let jsdomCleanUp: () => void;

beforeEach(() => {
  jsdomCleanUp = jsdomGlobal();
})

afterEach(() => {
  jsdomCleanUp();
})