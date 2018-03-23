import React from 'react';
import { simpleRestClient, Admin, Resource } from 'admin-on-rest';
import { Delete } from 'admin-on-rest/lib/mui';

import {
    CategoryList,
    CategoryCreate,
    CategoryShow,
} from './Category';

import {
    List,
} from './';

import {
    UserList,
    UserEdit,
    UserShow,
    UserCreate,
} from './User';

import {
    PetCreate,
    PetEdit,
    PetShow,
} from './Pet';



const App = () => (
    <Admin title={"demo"} restClient={simpleRestClient}>
        <Resource
            name="categorys"
            list={ CategoryList }
            create={ CategoryCreate }
            show={ CategoryShow }
            remove={Delete}
        />
        <Resource
            name="pets"
            list={ List }
            remove={Delete}
        />
        <Resource
            name="users"
            list={ UserList }
            edit={ UserEdit }
            show={ UserShow }
            create={ UserCreate }
            remove={Delete}
        />
        <Resource
            name="pets"
            create={ PetCreate }
            edit={ PetEdit }
            show={ PetShow }
            remove={Delete}
        />
    </Admin>
)

export default App;