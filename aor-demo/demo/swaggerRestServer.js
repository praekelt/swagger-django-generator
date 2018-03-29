/**
 * Generated swaggerRestServer.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import { stringify } from 'query-string';
import { fetchUtils } from 'admin-on-rest';

export const GET_LIST = 'GET_LIST';
export const GET_ONE = 'GET_ONE';
export const GET_MANY = 'GET_MANY';
export const GET_MANY_REFERENCE = 'GET_MANY_REFERENCE';
export const CREATE = 'CREATE';
export const UPDATE = 'UPDATE';
export const DELETE = 'DELETE';


/**
 * @param {String} apiUrl The base API url
 * @param {String} type One of the constants appearing at the top if this file, e.g. 'UPDATE'
 * @param {String} resource Name of the resource to fetch, e.g. 'posts'
 * @param {Object} params The REST request params, depending on the type
 * @returns {Object} { url, options } The HTTP request parameters
 */
export const convertRESTRequestToHTTP = ({
    apiUrl,
    type,
    resource,
    params
}) => {
    let url = '';
    const options = {};
    const query = {};

    switch (type) {
        case GET_MANY_REFERENCE: {
            query[params.target] = params.id;
            break;
        }
        case GET_LIST: {
            if (params.pagination) {
                const { page, perPage } = params.pagination;
                query['limit'] = perPage;
                query['offset'] = (page - 1) * perPage;
            }

            if (params.sort) {
                const { field, order } = params.sort;
                query['ordering'] = `${order === 'DESC' ? '-' : ''}` + field;
            }

            if (params.filter) {
                Object.keys(params.filter).forEach(key => {
                    query[key] = params.filter[key];
                });
            }

            url = `${apiUrl}/${resource}?${stringify(query)}`;
            break;
        }
        case GET_ONE:
            url = `${apiUrl}/${resource}/${params.id}`;
            break;
        case GET_MANY: {
            const query = {
                filter: JSON.stringify({ id: params.ids }),
            };
            url = `${apiUrl}/${resource}?${stringify(query)}`;
            break;
        }
        case UPDATE:
            url = `${apiUrl}/${resource}/${params.id}`;
            options.method = 'PUT';
            options.body = JSON.stringify(params.data);
            break;
        case CREATE:
            url = `${apiUrl}/${resource}`;
            options.method = 'POST';
            options.body = JSON.stringify(params.data);
            break;
        case DELETE:
            url = `${apiUrl}/${resource}/${params.id}`;
            options.method = 'DELETE';
            break;
        default:
            throw new Error(`Unsupported fetch action type ${type}`);
    }
    return { url, options };
};

/**
 * @param {Object} response HTTP response from fetch()
 * @param {String} type One of the constants appearing at the top if this file, e.g. 'UPDATE'
 * @param {String} resource Name of the resource to fetch, e.g. 'posts'
 * @param {Object} params The REST request params, depending on the type
 * @returns {Object} REST response
 */
const convertHTTPResponseToREST = ({ response, type, resource, params }) => {
    const { headers, json } = response;

    switch (type) {

        // Total required by AOR for all list operations
        case GET_LIST:
            if (resource in COMPOSITE_KEY_RESOURSES) {
                let keys = COMPOSITE_KEY_RESOURSES[resource];
                return {
                    data: json ? json.map(res => ({ ...res, id: `${keys.map(key => res[key]).join('/')}` })) : json,
                    total: 10
                }
            }
        case GET_MANY_REFERENCE:
            if (!headers.has('x-total-count')) {
                throw new Error(
                    'The X-Total-Count header is missing in the HTTP Response. The jsonServer REST client expects responses for lists of resources to contain this header with the total number of results to build the pagination. If you are using CORS, did you declare X-Total-Count in the Access-Control-Expose-Headers header?'
                );
            }
            return {
                data: json,
                total: parseInt(
                    headers
                        .get('x-total-count')
                        .split('/')
                        .pop(),
                    10
                ),
            };
        case CREATE:
            return { data: { ...params.data, id: json.id } };
        default:
            return { data: json };
    }
};

/**
 * Maps admin-on-rest queries to a Swagger Spec
 * @example
 * GET_LIST     => GET http://my.api.url/users?limit=10&offset=30&ordering=-name
 * GET_ONE      => GET http://my.api.url/users/123/ or GET http://my.api.url/users/123/321/ in the case of a composite key
 * GET_MANY     => GET http://my.api.url/users/1/ GET http://my.api.url/users/2/
 * UPDATE       => PUT http://my.api.url/users/123/ or PUT http://my.api.url/users/123/321/ in the case of a composite key
 * CREATE       => POST http://my.api.url/users/
 * DELETE       => DELETE http://my.api.url/users/123/ or DELETE http://my.api.url/users/123/321/ in the case of a composite key
 */
export default (apiUrl, httpClient = fetchUtils.fetchJson) => {
    /**
     * @param {string} type Request type, e.g GET_LIST
     * @param {string} resource Resource name, e.g. "users"
     * @param {Object} payload Request parameters. Depends on the request type
     * @returns {Promise} the Promise for a REST response
     */

    return async (type, resource, params) => {
        const { url, options } = convertRESTRequestToHTTP({
            apiUrl,
            type,
            resource,
            params
        });

        return httpClient(url, options).then(response =>
            convertHTTPResponseToREST({
                response,
                type,
                resource,
                params
            })
        );
    };
};
/** End of Generated Code **/