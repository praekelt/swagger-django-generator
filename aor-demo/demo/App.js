import React from 'react';
import { Admin, Delete, Resource } from 'admin-on-rest';
import swaggerRestServer from './swaggerRestServer';

import {
    PetEdit,
    PetShow,
    PetCreate,
} from './Pet';

import {
    List,
} from './';

import {
    CategoryList,
    CategoryShow,
    CategoryCreate,
} from './Category';

import {
    UserList,
    UserShow,
    UserCreate,
    UserEdit,
} from './User';



const App = () => (
    <Admin title={"demo"} restClient={swaggerRestServer('rest-url:port')}>
        <Resource
            name="pets"
            edit={ PetEdit }
            show={ PetShow }
            create={ PetCreate }
            remove={Delete}
        />
        <Resource
            name="pets"
            list={ List }
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
            create={ UserCreate }
            edit={ UserEdit }
            remove={Delete}
        />
    </Admin>
)

export default App;