import React from 'react';
import { simpleRestClient, Admin, Resource } from 'admin-on-rest';
import { Delete } from 'admin-on-rest/lib/mui';

import { 
    OrderList,
    OrderShow,
    OrderCreate,
    OrderEdit
} from './Order';
import { 
    PetList,
    PetShow,
    PetCreate,
    PetEdit
} from './Pet';
import { 
    CategoryList,
    CategoryShow,
    CategoryCreate
} from './Category';
import { 
    UserList,
    UserShow,
    UserCreate,
    UserEdit
} from './User';
import { 
    TagList,
    TagShow,
    TagEdit
} from './Tag';


const App = () => (
    <Admin title={"demo"} restClient={simpleRestClient}>
        <Resource
            name={"Order"}
            list={ OrderList }
            show={ OrderShow }
            create={ OrderCreate }
            edit={ OrderEdit}
            remove={Delete}
        />
        <Resource
            name={"Pet"}
            list={ PetList }
            show={ PetShow }
            create={ PetCreate }
            edit={ PetEdit}
            remove={Delete}
        />
        <Resource
            name={"Category"}
            list={ CategoryList }
            show={ CategoryShow }
            create={ CategoryCreate }
            remove={Delete}
        />
        <Resource
            name={"User"}
            list={ UserList }
            show={ UserShow }
            create={ UserCreate }
            edit={ UserEdit}
            remove={Delete}
        />
        <Resource
            name={"Tag"}
            list={ TagList }
            show={ TagShow }
            edit={ TagEdit}
            remove={Delete}
        />
    </Admin>
)

export default App;