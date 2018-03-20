import React from 'react';
import { simpleRestClient, Admin, Resource } from 'admin-on-rest';
import { Delete } from 'admin-on-rest/lib/mui';

import { 
    TagList,
    TagShow,
    TagEdit
} from './tag';
import { 
    PetList,
    PetShow,
    PetCreate,
    PetEdit
} from './pet';
import { 
    UserList,
    UserShow,
    UserCreate,
    UserEdit
} from './user';
import { 
    OrderList,
    OrderShow,
    OrderCreate,
    OrderEdit
} from './order';
import { 
    CategoryList,
    CategoryShow,
    CategoryCreate
} from './category';


const App = () => (
    <Admin title={"demo"} restClient={simpleRestClient}>
        <Resource
            name="tag"
            list={ TagList }
            show={ TagShow }
            edit={ TagEdit}
            remove={Delete}
        />
        <Resource
            name="pet"
            list={ PetList }
            show={ PetShow }
            create={ PetCreate }
            edit={ PetEdit}
            remove={Delete}
        />
        <Resource
            name="user"
            list={ UserList }
            show={ UserShow }
            create={ UserCreate }
            edit={ UserEdit}
            remove={Delete}
        />
        <Resource
            name="order"
            list={ OrderList }
            show={ OrderShow }
            create={ OrderCreate }
            edit={ OrderEdit}
            remove={Delete}
        />
        <Resource
            name="category"
            list={ CategoryList }
            show={ CategoryShow }
            create={ CategoryCreate }
            remove={Delete}
        />
    </Admin>
)

export default App;