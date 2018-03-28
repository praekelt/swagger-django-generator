/**
 * Generated App.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import { cyan500, cyan300 } from 'material-ui/styles/colors';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import { Admin, Delete, Resource } from 'admin-on-rest';
import swaggerRestServer from './swaggerRestServer';
import authClient from './authClient';

import {
    PetList,
    PetCreate,
    PetShow,
    PetEdit,
} from './Pet';

import {
    UserList,
    UserCreate,
    UserShow,
    UserEdit,
} from './User';

import {
    CategoryList,
    CategoryCreate,
    CategoryShow,
} from './Category';



const App = () => (
    <Admin title="demo" theme={getMuiTheme(muiTheme)} restClient={swaggerRestServer('rest-url:port')} authClient={authClient}>
        <Resource
            name="pets"
            list={ PetList }
            create={ PetCreate }
            show={ PetShow }
            edit={ PetEdit }
            remove={Delete}
        />
        <Resource
            name="users"
            list={ UserList }
            create={ UserCreate }
            show={ UserShow }
            edit={ UserEdit }
            remove={Delete}
        />
        <Resource
            name="categories"
            list={ CategoryList }
            create={ CategoryCreate }
            show={ CategoryShow }
            remove={Delete}
        />
    </Admin>
)

const muiTheme = getMuiTheme({
    palette: {
        primary1Color: cyan500,
        accent1Color: cyan300
    }
});

export default App;
/** End of Generated Code **/