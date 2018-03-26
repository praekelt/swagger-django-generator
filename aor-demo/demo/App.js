import React from 'react';
import { Admin, Delete, Resource } from 'admin-on-rest';
import swaggerRestServer from './swaggerRestServer';

import {
    PetList,
    PetShow,
    PetEdit,
    PetCreate,
} from './Pet';

import {
    CategoryList,
    CategoryShow,
    CategoryCreate,
} from './Category';

import {
    UserList,
    UserShow,
    UserEdit,
    UserCreate,
} from './User';



const App = () => (
    <Admin title={"demo"} restClient={swaggerRestServer('rest-url:port')}>
        <Resource
            name="pets"
            list={ PetList }
            show={ PetShow }
            edit={ PetEdit }
            create={ PetCreate }
            remove={Delete}
        />
        <Resource
            name="categories"
            list={ CategoryList }
            show={ CategoryShow }
            create={ CategoryCreate }
            remove={Delete}
        />
        <Resource
            name="users"
            list={ UserList }
            show={ UserShow }
            edit={ UserEdit }
            create={ UserCreate }
            remove={Delete}
        />
    </Admin>
)

export default App;