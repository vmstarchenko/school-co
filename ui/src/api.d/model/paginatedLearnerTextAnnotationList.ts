/**
 * 
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { LearnerTextAnnotation } from './learnerTextAnnotation';


export interface PaginatedLearnerTextAnnotationList { 
    count?: number;
    next?: string | null;
    previous?: string | null;
    results?: Array<LearnerTextAnnotation>;
}

